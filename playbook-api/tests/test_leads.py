import sqlite3

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def cliente(tmp_path, monkeypatch):
    ruta = tmp_path / "leads.sqlite"
    monkeypatch.setenv("LEADS_DB", str(ruta))
    from main import app

    return TestClient(app), ruta


def filas(ruta):
    base = sqlite3.connect(ruta)
    base.row_factory = sqlite3.Row
    return [dict(f) for f in base.execute("SELECT * FROM leads")]


def test_el_mail_y_el_telefono_quedan_en_la_misma_fila(cliente):
    c, ruta = cliente
    assert c.post("/api/leads", json={"email": " Ana@Mail.com ", "origen": "hero"}).status_code == 200
    assert c.post("/api/leads/telefono", json={"email": "ana@mail.com", "telefono": "+54 9 11 1234-5678"}).status_code == 200
    (fila,) = filas(ruta)
    assert fila["email"] == "ana@mail.com"
    assert fila["telefono"] == "+5491112345678"
    assert fila["origen"] == "hero"


def test_repetir_el_mail_no_duplica_ni_borra_el_telefono(cliente):
    c, ruta = cliente
    c.post("/api/leads", json={"email": "ana@mail.com"})
    c.post("/api/leads/telefono", json={"email": "ana@mail.com", "telefono": "1112345678"})
    c.post("/api/leads", json={"email": "ana@mail.com"})
    (fila,) = filas(ruta)
    assert fila["telefono"] == "1112345678"


@pytest.mark.parametrize("email", ["ana", "ana@", "a b@mail.com", "ana@mail"])
def test_rechaza_mails_invalidos(cliente, email):
    c, _ = cliente
    assert c.post("/api/leads", json={"email": email}).status_code == 422


@pytest.mark.parametrize("telefono", ["123", "1" * 16, "sin numero"])
def test_rechaza_telefonos_invalidos(cliente, telefono):
    c, _ = cliente
    c.post("/api/leads", json={"email": "ana@mail.com"})
    assert c.post("/api/leads/telefono", json={"email": "ana@mail.com", "telefono": telefono}).status_code == 422


def test_telefono_sin_mail_previo_no_crea_nada(cliente):
    c, ruta = cliente
    assert c.post("/api/leads/telefono", json={"email": "x@mail.com", "telefono": "1112345678"}).status_code == 422
    assert filas(ruta) == []


def test_la_trampa_para_bots_no_guarda(cliente):
    c, ruta = cliente
    assert c.post("/api/leads", json={"email": "bot@mail.com", "sitio": "x"}).status_code == 200
    assert not ruta.exists()

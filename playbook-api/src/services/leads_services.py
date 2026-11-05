"""Reglas del optin: el mail entra primero y el teléfono se suma después a la misma fila."""

import re
from datetime import datetime, timezone

from src.db import conexion

_MAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]{2,}$")
_ORIGENES = {"hero", "adentro", "cierre"}


class DatoInvalido(ValueError):
    pass


def _ahora() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _mail(email: str) -> str:
    limpio = email.strip().lower()
    if len(limpio) > 254 or not _MAIL.match(limpio):
        raise DatoInvalido("Revisá el mail.")
    return limpio


def guardar_email(email: str, origen: str | None = None) -> None:
    limpio, ahora = _mail(email), _ahora()
    origen = origen if origen in _ORIGENES else None
    with conexion() as base:
        base.execute(
            """INSERT INTO leads (email, origen, creado_en, actualizado_en) VALUES (?, ?, ?, ?)
               ON CONFLICT(email) DO UPDATE SET actualizado_en = excluded.actualizado_en""",
            (limpio, origen, ahora, ahora),
        )


def guardar_telefono(email: str, telefono: str) -> None:
    limpio = _mail(email)
    digitos = re.sub(r"\D", "", telefono)
    if not 8 <= len(digitos) <= 15:
        raise DatoInvalido("Revisá el número.")
    numero = "+" + digitos if telefono.strip().startswith("+") else digitos
    with conexion() as base:
        fila = base.execute(
            "UPDATE leads SET telefono = ?, actualizado_en = ? WHERE email = ?",
            (numero, _ahora(), limpio),
        )
        if fila.rowcount == 0:
            raise DatoInvalido("Falta el mail.")

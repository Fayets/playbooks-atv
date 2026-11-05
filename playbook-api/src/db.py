"""La base es un archivo SQLite; la ruta llega por LEADS_DB y en el VPS vive fuera del repo."""

import os
import sqlite3
from contextlib import contextmanager

ESQUEMA = """
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    telefono TEXT,
    origen TEXT,
    creado_en TEXT NOT NULL,
    actualizado_en TEXT NOT NULL
)
"""


@contextmanager
def conexion():
    base = sqlite3.connect(os.environ.get("LEADS_DB", "leads.sqlite"), timeout=10)
    base.row_factory = sqlite3.Row
    try:
        base.execute("PRAGMA journal_mode=WAL")
        base.execute(ESQUEMA)
        with base:
            yield base
    finally:
        base.close()

"""API de playbook.atvos.io: guarda los mails y teléfonos del optin en un archivo SQLite."""

from fastapi import FastAPI

from src.controllers.leads_controller import router as leads_router

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
app.include_router(leads_router, prefix="/api/leads")

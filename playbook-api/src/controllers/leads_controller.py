"""Los dos pasos del optin. El campo `sitio` es una trampa: lo completan solo los bots."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from src.services import leads_services as leads

router = APIRouter()


class Mail(BaseModel):
    email: str = Field(max_length=254)
    origen: str | None = Field(default=None, max_length=20)
    sitio: str | None = Field(default=None, max_length=200)


class Telefono(BaseModel):
    email: str = Field(max_length=254)
    telefono: str = Field(max_length=30)


@router.post("")
def recibir_mail(datos: Mail) -> dict:
    if datos.sitio:
        return {"ok": True}
    try:
        leads.guardar_email(datos.email, datos.origen)
    except leads.DatoInvalido as error:
        raise HTTPException(status_code=422, detail=str(error))
    return {"ok": True}


@router.post("/telefono")
def recibir_telefono(datos: Telefono) -> dict:
    try:
        leads.guardar_telefono(datos.email, datos.telefono)
    except leads.DatoInvalido as error:
        raise HTTPException(status_code=422, detail=str(error))
    return {"ok": True}

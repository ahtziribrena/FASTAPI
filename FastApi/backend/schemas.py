from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional  # Necesario para los campos opcionales

class FichaBase(BaseModel):
    numero: str
    status: str
    grupo: Optional[str] = None  # Permite que sea None (NULL en la base de datos)
    fecha_solicitud: date
    tipo: str
    lugar: str
    alumno_id: int
    ciclo_id: int
    carrera_id: int
    configuracion_aspirante_id: Optional[int] = None  # Permite que sea None (NULL en la base de datos)

class FichaCreate(FichaBase):
    pass

class Ficha(FichaBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

from sqlalchemy import Column, Integer, String, Date, DateTime
from .database import Base

class Ficha(Base):
    __tablename__ = "fichas"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    numero = Column(String)
    status = Column(String)
    grupo = Column(String)
    fecha_solicitud = Column(Date)
    tipo = Column(String)
    lugar = Column(String)
    alumno_id = Column(Integer, nullable=False)
    ciclo_id = Column(Integer, nullable=False)
    carrera_id = Column(Integer, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    configuracion_aspirante_id = Column(Integer, nullable=False)  # Nombre correcto
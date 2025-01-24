from sqlalchemy.orm import Session
from backend.models import fichas_models
from backend.schemas import schema_fichas

def get_ficha(db: Session, ficha_id: int):
    return db.query(fichas_models.Ficha).filter(fichas_models.Ficha.id == ficha_id).first()

def get_fichas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(fichas_models.Ficha).offset(skip).limit(limit).all()

def create_ficha(db: Session, ficha: schema_fichas.FichaCreate):
    db_ficha = fichas_models.Ficha(
        numero=ficha.numero,
        status=ficha.status,
        grupo=ficha.grupo,
        fecha_solicitud=ficha.fecha_solicitud,
        tipo=ficha.tipo,
        lugar=ficha.lugar,
        alumno_id=ficha.alumno_id,
        ciclo_id=ficha.ciclo_id,
        carrera_id=ficha.carrera_id,
        created_at=ficha.created_at,
        updated_at=ficha.updated_at,
        configuracion_aspirante_id=ficha.configuracion_aspirante_id
    )
    db.add(db_ficha)
    db.commit()
    db.refresh(db_ficha)
    return db_ficha

def remove_ficha(db: Session, ficha_id:int):
    db_ficha = get_ficha(db=db, ficha_id=ficha_id)
    db.delete(db_ficha)
    db.commit()

def update_ficha(db: Session, ficha_id: int, ficha: schema_fichas.FichaCreate):
    db_ficha = get_ficha(db=db, ficha_id=ficha_id)
    if db_ficha is None:
        return None

    # Actualizar los atributos de la instancia existente
    db_ficha.numero = ficha.numero
    db_ficha.status = ficha.status
    db_ficha.grupo = ficha.grupo
    db_ficha.fecha_solicitud = ficha.fecha_solicitud
    db_ficha.tipo = ficha.tipo
    db_ficha.lugar = ficha.lugar
    db_ficha.alumno_id = ficha.alumno_id
    db_ficha.ciclo_id = ficha.ciclo_id
    db_ficha.carrera_id = ficha.carrera_id
    db_ficha.configuracion_aspirante_id = ficha.configuracion_aspirante_id
    db_ficha.updated_at = ficha.updated_at  # Asegúrate de actualizar la fecha

    db.commit()
    db.refresh(db_ficha)
    return db_ficha
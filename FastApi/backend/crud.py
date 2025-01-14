from sqlalchemy.orm import Session
from . import models, schemas

def get_ficha(db: Session, ficha_id: int):
    return db.query(models.Ficha).filter(models.Ficha.id == ficha_id).first()

def get_fichas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ficha).offset(skip).limit(limit).all()

def create_ficha(db: Session, ficha: schemas.FichaCreate):
    db_ficha = models.Ficha(
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
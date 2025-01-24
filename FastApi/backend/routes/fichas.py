from fastapi import FastAPI, Depends, HTTPException
from fastapi import APIRouter
from sqlalchemy.orm import Session
from backend import database
from backend.database import get_db, validate_connection,Base
from backend.models import fichas_models
from backend.schemas import schema_fichas
from backend.services import service_fichas
fichas_models.Base.metadata.create_all(bind=database.engine)

router = APIRouter()

@router.post("/fichas/", response_model=schema_fichas.Ficha)
def create_ficha(ficha: schema_fichas.FichaCreate, db: Session = Depends(get_db)):
    return service_fichas.create_ficha(db=db, ficha=ficha)

@router.get("/fichas/{ficha_id}", response_model=schema_fichas.Ficha)
def read_ficha(ficha_id: int, db: Session = Depends(get_db)):
    db_ficha = service_fichas.get_ficha(db, ficha_id=ficha_id)
    if db_ficha is None:
        raise HTTPException(status_code=404, detail="Ficha not found")
    return db_ficha

@router.get("/fichas/", response_model=list[schema_fichas.Ficha])
def read_fichas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    fichas = service_fichas.get_fichas(db, skip=skip, limit=limit)
    return fichas

@router.delete("/fichas/{ficha_id}", response_model=schema_fichas.Ficha)
def delete_ficha(ficha_id: int, db: Session = Depends(get_db)):
    db_ficha = service_fichas.get_ficha(db, ficha_id=ficha_id)
    if db_ficha is None:
        raise HTTPException(status_code=404, detail="Ficha not found")
    service_fichas.remove_ficha(db, ficha_id=ficha_id)
    return db_ficha

@router.put("/fichas/{ficha_id}", response_model=schema_fichas.Ficha)
def update_ficha(ficha_id: int, ficha: schema_fichas.FichaCreate, db: Session = Depends(get_db)):
    db_ficha = service_fichas.update_ficha(db, ficha_id=ficha_id, ficha=ficha)
    if db_ficha is None:
        raise HTTPException(status_code=404, detail="Ficha not found")
    return db_ficha

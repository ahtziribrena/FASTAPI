from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/fichas/", response_model=schemas.Ficha)
def create_ficha(ficha: schemas.FichaCreate, db: Session = Depends(get_db)):
    return crud.create_ficha(db=db, ficha=ficha)

@app.get("/fichas/{ficha_id}", response_model=schemas.Ficha)
def read_ficha(ficha_id: int, db: Session = Depends(get_db)):
    db_ficha = crud.get_ficha(db, ficha_id=ficha_id)
    if db_ficha is None:
        raise HTTPException(status_code=404, detail="Ficha not found")
    return db_ficha

@app.get("/fichas/", response_model=list[schemas.Ficha])
def read_fichas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    fichas = crud.get_fichas(db, skip=skip, limit=limit)
    return fichas

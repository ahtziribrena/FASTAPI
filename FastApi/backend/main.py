from backend.models import fichas_models
from backend.routes import fichas
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text  # Asegúrate de importar text
from backend.database import get_db, validate_connection

app = FastAPI()
app.include_router(fichas.router)
# Validar la conexión al iniciar la aplicación
validate_connection()

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    try:
        # Realiza una consulta para verificar la conectividad
        result = db.execute(text("SELECT 1")).fetchall()
        
        # Extraer los valores de la consulta como una lista
        result_list = [row[0] for row in result]  # Convertir el resultado a lista

        return {"message": "Conexión exitosa", "result": result_list}
    except Exception as e:
        return {"message": f"Error en la conexión: {str(e)}"}




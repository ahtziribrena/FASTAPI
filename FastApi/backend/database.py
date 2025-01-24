from sqlalchemy import create_engine, text  # Asegúrate de importar text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from sqlalchemy.exc import OperationalError, SQLAlchemyError

load_dotenv()

# Definir la URL de la base de datos
DATABASE_URL = f"postgresql://{os.getenv('NES_DB_USER')}:{os.getenv('NES_DB_PASSWORD')}@{os.getenv('NES_DB_HOST')}:{os.getenv('NES_DB_PORT')}/{os.getenv('NES_DB_NAME')}"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def validate_connection():
    try:
        # Usar la sesión en lugar de la conexión directa
        with SessionLocal() as session:
            # Usar text() para envolver la consulta
            result = session.execute(text("SELECT 1"))  # Ejecutar la consulta como texto
            print(f"Resultado de la consulta: {result.fetchone()}")
        print("Conexión a la base de datos exitosa.")
    except OperationalError as e:
        print(f"\nError de conexión a la base de datos: {e}")
    except SQLAlchemyError as e:
        print(f"\nError inesperado de SQLAlchemy: {e}")

def get_db():
    db = SessionLocal()
    try:
        yield db
    except OperationalError as e:
        print(f"\nError de conexión a la base de datos: {e}")
        print(f"\nDATABASE_URL: {DATABASE_URL}")  # Puedes ocultar esta línea en producción
    except SQLAlchemyError as e:
        print(f"\nError inesperado de SQLAlchemy: {e}")
    finally:
        db.close()

# Validar la conexión al iniciar
validate_connection()


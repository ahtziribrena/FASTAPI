from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from sqlalchemy.exc import OperationalError, SQLAlchemyError

load_dotenv()

DATABASE_URL = f"postgresql://{os.getenv('NES_DB_USER')}:{os.getenv('NES_DB_PASSWORD')}@{os.getenv('NES_DB_HOST')}:{os.getenv('NES_DB_PORT')}/{os.getenv('NES_DB_NAME')}"

# Imprimir DATABASE_URL para verificar la conexión
print("\n ---------------------------------------------------------------------------DATABASE_URL:", DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    print("\n-----------holasss\n")
    db = SessionLocal()  # Asumo que SessionLocal está previamente configurado
    try:
        print("\n-----------try\n")
        yield db
        print("\n-----------------------------------conexion exitosa\n")
    except OperationalError as e:
        print ("\n sql-------------------------------\n")
        print(f"\nError de conexión a la base de datos: {e}")
        print(f"\nDATABASE_URL: {DATABASE_URL}")  # Asegúrate de que DATABASE_URL está definido
    except SQLAlchemyError as e:
        print ("\n alchemy-------------------------------\n")
        print(f"\nError inesperado de SQLAlchemy: {e}")
    finally:
        db.close()
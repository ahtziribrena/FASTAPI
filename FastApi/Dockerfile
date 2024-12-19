# Dockerfile para Pandas
FROM python:3.11

WORKDIR /app

# Copia los archivos de requirements
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente
COPY . .

CMD ["uvicorn", "proyecto.main:app", "--host", "0.0.0.0", "--port", "8000"]

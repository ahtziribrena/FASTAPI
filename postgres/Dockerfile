FROM postgres:14.6 AS postgres_base

FROM postgres_base AS database
LABEL name=pandas_database version=1.0

# Copia la carpeta con los scripts SQL al directorio de inicialización
COPY databases_backups /docker-entrypoint-initdb.d/sql-scripts

# Copia un script para crear bases de datos y usuarios y ejecutar los archivos .sql
COPY init.sh /docker-entrypoint-initdb.d/

# Otorga permisos de ejecución al script de inicialización
RUN chmod +x /docker-entrypoint-initdb.d/init.sh

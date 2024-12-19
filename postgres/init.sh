#!/bin/bash
set -e

# Crear bases de datos y usuarios
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE nes_db;
    CREATE USER nes_user WITH ENCRYPTED PASSWORD 'nes_escolares';

    CREATE DATABASE inscripciones_db;
    CREATE USER inscripciones_user WITH ENCRYPTED PASSWORD 'inscripciones';

EOSQL

# Ejecutar scripts SQL para cada base de datos
for db in /docker-entrypoint-initdb.d/sql-scripts/*; do
    db_name=$(basename $db)
    for f in $db/*.sql; do
        echo "Running $f on $db_name"
        psql -U "$POSTGRES_USER" -d "$db_name" -f "$f"
    done
done

#!/bin/bash

echo "Aguardando o banco de dados iniciar..."
while ! mysqladmin ping -h "db" --silent; do
    sleep 2
done

echo "Banco de dados está pronto! Iniciando a aplicação..."

echo "Ativando ambiente Conda...."
source /opt/conda/bin/activate tmdb_env
conda info --envs

python -c "import mysql.connector; print('MySQL Connector Funcionando!')"

python main.py
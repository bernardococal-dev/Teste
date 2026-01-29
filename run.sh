#!/bin/bash

# Instalar dependências
echo "Instalando dependências..."
pip install -r requirements.txt

# Executar a aplicação Flask
echo "Iniciando a aplicação..."
python app.py

#!/data/data/com.termux/files/usr/bin/bash

echo "🔁 Atualizando a Egregoro via GitHub..."
git pull origin main

echo "🚀 Iniciando a API da Egregoro..."
python3 egregoro_api.py

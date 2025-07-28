#!/bin/bash

# Script para salvar alterações no GitHub

MENSAGEM=${1:-"Atualização automática"}

echo "[*] Adicionando arquivos alterados..."
git add .

echo "[*] Fazendo commit..."
git commit -m "$MENSAGEM"

echo "[*] Atualizando com mudanças do GitHub..."
git pull --rebase origin main

echo "[*] Enviando para o GitHub..."
git push origin main

echo "[✓] Projeto Egregoro salvo com sucesso no GitHub!"

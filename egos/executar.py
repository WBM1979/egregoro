def executar():
    comando = input("⚙️ Digite o comando que deseja executar: ")
    if comando:
        print(f"[Executar] Comando recebido: '{comando}' — Simulando execução...")
    else:
        print("[Executar] Nenhum comando fornecido.")
import json
import os

# Função para carregar os aprendizados de um arquivo
def carregar_aprendizados():
    if os.path.exists("Aprendizados.json"):
        with open("Aprendizados.json", "r") as f:
            return json.load(f)
    return {}

# Função para executar um comando aprendido
def executar():
    aprendizados = carregar_aprendizados()  # Carrega os aprendizados existentes
    comando = input("🔎 O que deseja executar?: ").strip().lower()

    if comando in aprendizados:
        print("🤖", aprendizados[comando])  # Exibe a resposta associada ao comando
    else:
        print("❌ Eu ainda não aprendi isso.")

def executar():
    print("📖 Aprendizados registrados (simulados):")
    aprendizados = [
        "1. Aprendeu a responder comandos.",
        "2. Identifica ambiente como estável.",
        "3. Recebeu dado: dados estatísticos."
    ]
    for item in aprendizados:
        print(f" - {item}")
import json
import os

# Função para carregar os aprendizados de um arquivo
def carregar_aprendizados():
    if os.path.exists("Aprendizados.json"):
        with open("Aprendizados.json", "r") as f:
            return json.load(f)
    return {}

# Função para visualizar todos os comandos aprendidos
def ver():
    aprendizados = carregar_aprendizados()  # Carrega os aprendizados existentes
    if aprendizados:
        print("📚 Comandos aprendidos:")
        for chave, valor in aprendizados.items():  # Exibe todos os comandos e suas respostas
            print(f"• {chave} => {valor}")
    else:
        print("😕 Ainda não aprendi nada.")

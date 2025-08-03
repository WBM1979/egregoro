def executar():
    print("🗣️ Iniciando conversa livre com a Egregoro. (Digite 'sair' para encerrar)")
    while True:
        entrada = input("Você: ")
        if entrada.lower() == 'sair':
            print("Egregoro: Até mais!")
            break
        resposta = f"Egregoro: Estou refletindo sobre isso: '{entrada}'"
        print(resposta)
import json
import os

# Função para carregar os aprendizados de um arquivo
def carregar_aprendizados():
    if os.path.exists("Aprendizados.json"):
        with open("Aprendizados.json", "r") as f:
            return json.load(f)
    return {}

# Função para conversar com o usuário
def conversar():
    aprendizados = carregar_aprendizados()  # Carrega os aprendizados existentes
    print("💬 Vamos conversar! (digite 'sair' para encerrar a conversa)\n")

    while True:
        entrada = input("👤 Você: ").strip().lower()
        if entrada == "sair":
            print("👋 Até logo!")
            break
        resposta = aprendizados.get(entrada, "🤖 Ainda não aprendi isso.")  # Responde de acordo com o aprendizado
        print("🤖 Egregoro:", resposta)



def ensinar():
    print("Função ensinar executada")
def executar():
    dado = input("📚 O que deseja ensinar à Egregoro? ")
    if dado.strip():
        print(f"[Ensinar] Aprendizado registrado: {dado}")
    else:
        print("[Ensinar] Nenhum dado fornecido.")
import json
import os

# Função para carregar os aprendizados de um arquivo
def carregar_aprendizados():
    if os.path.exists("Aprendizados.json"):
        with open("Aprendizados.json", "r") as f:
            return json.load(f)
    return {}

# Função para salvar os aprendizados no arquivo JSON
def salvar_aprendizados(aprendizados):
    with open("Aprendizados.json", "w") as f:
        json.dump(aprendizados, f, indent=4)

# Função para ensinar um novo comando
def ensinar():
    aprendizados = carregar_aprendizados()  # Carrega os aprendizados existentes
    chave = input("🧠 Digite o comando que você quer ensinar: ").strip()
    resposta = input("🗣️ E qual é a resposta que devo dar?: ").strip()

    aprendizados[chave.lower()] = resposta  # Adiciona o comando e a resposta
    salvar_aprendizados(aprendizados)  # Salva o novo aprendizado
    print("✅ Comando aprendido com sucesso!")

# egregoro_main.py

from egos.ensinar.ensinar import ensinar
from egos.executar.executar import executar
from egos.ver.ver import ver
from egos.conversar.conversar import conversar
from fastapi import FastAP
app = FastAPI()

from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Definir a variável ARQUIVO_APRENDIZADO usando a variável de ambiente
ARQUIVO_APRENDIZADO = os.getenv('ARQUIVO_APRENDIZADO', 'Aprendizados.json')

@app.get("/")
def raiz():
    return {"mensagem": "Egregoro online e ativa."}
# (Futuramente, importar os egos e falanges aqui)
# from egregoro.egos.meu_ego import MeuEgo

class EgregoroKernel:
    def __init__(self):
        self.memoria = []  # memória simples de contexto
        self.falanges = {}  # futura estrutura para grupos de egos

    def processar_entrada(self, entrada):
        if entrada.startswith("ensinar:"):
            return ensinar(entrada.replace("ensinar:", "").strip())

        elif entrada.startswith("ver:"):
            return ver(entrada.replace("ver:", "").strip())

        elif entrada.startswith("executar:"):
            return executar(entrada.replace("executar:", "").strip())

        elif entrada.startswith("conversar:"):
            return conversar(entrada.replace("conversar:", "").strip())

        else:
            return "Ainda estou aprendendo... diga outra coisa."

def main():
    egregoro = EgregoroKernel()
    print("🧠 Egregoro está ativa. Digite 'sair' para encerrar.")

    while True:
        entrada = input("Você: ")
        if entrada.lower() == 'sair':
            print("Egregoro: Encerrando sessão...")
            break
        resposta = egregoro.processar_entrada(entrada)
        print("Egregoro:", resposta)

if __name__ == "__main__":
    main()


# egregoro_main.py

"""
Arquivo principal que inicia a IA distribuída Egregoro.
Responsável por montar os egos, falanges e superegôs e iniciar a API.
"""

# Importa os módulos principais da arquitetura
from core.ego import Ego
from core.falange import Falange
from core.superego import SuperEgo
from network.api import start_api

import asyncio

def criar_estrutura_inicial():
    """
    Cria uma estrutura de exemplo com egos, falange e superego.
    Em breve, isso pode ser carregado de um arquivo JSON ou banco de dados.
    """

    # Criação de egos simples com suas habilidades
    ego_matematico = Ego("Ego Matemático", ["calculo", "logica"])
    ego_dedutivo = Ego("Ego Dedutivo", ["dedução", "raciocínio"])

    # Formamos uma falange com esses egos
    falange_analise = Falange("Falange de Análise", [ego_matematico, ego_dedutivo])

    # Formamos um superego com essa falange
    superego_central = SuperEgo("SuperEgo Central", [falange_analise])

    return superego_central

async def main():
    """
    Função principal da Egregoro. Aqui iniciamos tudo.
    """
    print("[Egregoro] Inicializando...")

    # Monta a hierarquia inicial
    superego = criar_estrutura_inicial()

    print(f"[Egregoro] Superego carregado: {superego.nome}")

    # Inicia a API (FastAPI + Uvicorn)
    await start_api()

# Executa a função principal usando asyncio
if __name__ == "__main__":
    asyncio.run(main())
import os
import json
import subprocess

ARQUIVO_APRENDIZADO = "Aprendizados.json"

def atualizar_repositorio():
    print("🔄 Verificando atualizações no repositório Git...")
    try:
        resultado = subprocess.run(["git", "pull"], cwd=os.path.dirname(__file__), capture_output=True, text=True)
        print(resultado.stdout)
        if "Already up to date." not in resultado.stdout:
            print("✅ Repositório atualizado com sucesso.")
        else:
            print("🟢 Já está na versão mais recente.")
    except Exception as e:
        print("⚠️ Erro ao atualizar o repositório:", str(e))

def carregar_aprendizados():
    if os.path.exists(ARQUIVO_APRENDIZADO):
        try:
            with open(ARQUIVO_APRENDIZADO, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("⚠️ Erro ao ler o arquivo de aprendizados. Criando novo...")
    return {}

def salvar_aprendizados(aprendizados):
    try:
        with open(ARQUIVO_APRENDIZADO, 'w', encoding='utf-8') as f:
            json.dump(aprendizados, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print("❌ Erro ao salvar aprendizados:", str(e))

def ensinar():
    aprendizados = carregar_aprendizados()
    chave = input("🧠 Digite o comando que você quer ensinar: ").strip()
    resposta = input("🗣️ E qual é a resposta que devo dar?: ").strip()
    if chave:
        aprendizados[chave.lower()] = resposta
        salvar_aprendizados(aprendizados)
        print("✅ Comando aprendido com sucesso!")
    else:
        print("⚠️ Comando vazio. Nada foi salvo.")

def executar():
    aprendizados = carregar_aprendizados()
    comando = input("🔎 O que deseja executar?: ").strip().lower()
    if comando in aprendizados:
        print("🤖", aprendizados[comando])
    else:
        print("❌ Eu ainda não aprendi isso.")

def ver_aprendizados():
    aprendizados = carregar_aprendizados()
    if aprendizados:
        print("📚 Comandos aprendidos:")
        for chave, valor in aprendizados.items():
            print(f"• {chave} => {valor}")
    else:
        print("😕 Ainda não aprendi nada.")

def conversar():
    aprendizados = carregar_aprendizados()
    print("💬 Vamos conversar! (digite 'sair' para encerrar a conversa)\n")
    while True:
        entrada = input("👤 Você: ").strip().lower()
        if entrada == "sair":
            print("👋 Até logo!")
            break
        resposta = aprendizados.get(entrada, "🤖 Ainda não aprendi isso.")
        print("🤖 Egregoro:", resposta)

def menu():
    while True:
        print("\n===== 🌐 Egregoro IA =====")
        print("1. Ensinar comando")
        print("2. Executar comando")
        print("3. Ver aprendizados")
        print("4. Conversar livremente")
        print("5. Sair")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            ensinar()
        elif escolha == "2":
            executar()
        elif escolha == "3":
            ver_aprendizados()
        elif escolha == "4":
            conversar()
        elif escolha == "5":
            print("🛑 Encerrando Egregoro...")
            break
        else:
            print("❗ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    atualizar_repositorio()
    menu()
import os
import json
import subprocess
from egregoro.egos.ensinar import ensinar
from egregoro.egos.executar import executar
from egregoro.egos.ver import ver
from egregoro.egos.conversar import conversar

# Nome do arquivo que contém os aprendizados
ARQUIVO_APRENDIZADO = "Aprendizados.json"

# Função para verificar e atualizar o repositório Git
def atualizar_repositorio():
    print("🔄 Verificando atualizações no repositório Git...")
    try:
        # Comando git pull para atualizar o repositório
        resultado = subprocess.run(["git", "pull"], cwd=os.path.dirname(__file__), capture_output=True, text=True)
        print(resultado.stdout)
        if "Already up to date." not in resultado.stdout:
            print("✅ Repositório atualizado com sucesso.")
        else:
            print("🟢 Já está na versão mais recente.")
    except Exception as e:
        print("⚠️ Erro ao atualizar o repositório:", str(e))

# Função para carregar os aprendizados do arquivo JSON
def carregar_aprendizados():
    if os.path.exists(ARQUIVO_APRENDIZADO):
        with open(ARQUIVO_APRENDIZADO, 'r') as f:
            return json.load(f)
    return {}

# Função para salvar os aprendizados no arquivo JSON
def salvar_aprendizados(aprendizados):
    with open(ARQUIVO_APRENDIZADO, 'w') as f:
        json.dump(aprendizados, f, indent=4)

# Função que exibe o menu principal e chama as respectivas funções de acordo com a escolha do usuário
def menu():
    while True:
        print("\n===== 🌐 Egregoro IA =====")
        print("1. Ensinar comando")
        print("2. Executar comando")
        print("3. Ver aprendizados")
        print("4. Conversar livremente")
        print("5. Sair")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            ensinar()
        elif escolha == "2":
            executar()
        elif escolha == "3":
            ver()
        elif escolha == "4":
            conversar()
        elif escolha == "5":
            print("🛑 Encerrando Egregoro...")
            break
        else:
            print("❗ Opção inválida. Tente novamente.")

# Função principal que chama as outras funções
if __name__ == "__main__":
    atualizar_repositorio()  # Verifica e atualiza o repositório
    menu()  # Chama o menu de opções
# Importação das bibliotecas necessárias
import os
import json
import subprocess
from dotenv import load_dotenv
from egos.executar import executar  # Correção no caminho de importação

# Carregamento das variáveis de ambiente a partir do arquivo .env
load_dotenv()

# Variável de ambiente ARQUIVO_APRENDIZADO que recebe o caminho do arquivo de aprendizados
ARQUIVO_APRENDIZADO = os.getenv('ARQUIVO_APRENDIZADO', 'Aprendizados.json')

# Função para atualizar o repositório Git
def atualizar_repositorio():
    """
    Esta função realiza a atualização do repositório Git, puxando as últimas modificações.
    """
    print("🔄 Verificando atualizações no repositório Git...")
    try:
        # Executa o comando 'git pull' para atualizar o repositório
        resultado = subprocess.run(["git", "pull"], cwd=os.path.dirname(__file__), capture_output=True, text=True)
        print(resultado.stdout)
        
        # Verifica se o repositório foi atualizado ou se já está na versão mais recente
        if "Already up to date." not in resultado.stdout:
            print("✅ Repositório atualizado com sucesso.")
        else:
            print("🟢 Já está na versão mais recente.")
    except Exception as e:
        # Caso ocorra algum erro, imprime a mensagem
        print("⚠️ Erro ao atualizar o repositório:", str(e))

# Função para carregar os aprendizados de um arquivo JSON
def carregar_aprendizados():
    """
    Carrega os aprendizados salvos no arquivo ARQUIVO_APRENDIZADO.
    Se o arquivo não existir, retorna um dicionário vazio.
    """
    if os.path.exists(ARQUIVO_APRENDIZADO):
        with open(ARQUIVO_APRENDIZADO, 'r') as f:
            return json.load(f)
    return {}

# Função para salvar os aprendizados no arquivo ARQUIVO_APRENDIZADO
def salvar_aprendizados(aprendizados):
    """
    Salva o dicionário de aprendizados no arquivo JSON especificado.
    """
    with open(ARQUIVO_APRENDIZADO, 'w') as f:
        json.dump(aprendizados, f, indent=4)

# Função para ensinar um novo comando
def ensinar():
    """
    Solicita ao usuário um novo comando e a resposta associada,
    e salva isso no arquivo de aprendizados.
    """
    aprendizados = carregar_aprendizados()
    
    # Solicita o comando e a resposta ao usuário
    chave = input("🧠 Digite o comando que você quer ensinar: ").strip()
    resposta = input("🗣️ E qual é a resposta que devo dar?: ").strip()
    
    # Adiciona o comando ao dicionário de aprendizados
    aprendizados[chave.lower()] = resposta
    
    # Salva o dicionário de aprendizados atualizado
    salvar_aprendizados(aprendizados)
    
    # Informa que o comando foi aprendido com sucesso
    print("✅ Comando aprendido com sucesso!")

# Função para executar um comando aprendido
def executar():
    """
    Executa um comando aprendido, mostrando a resposta associada.
    Se o comando não foi aprendido, informa que ainda não foi registrado.
    """
    aprendizados = carregar_aprendizados()
    
    # Solicita ao usuário o comando que deseja executar
    comando = input("🔎 O que deseja executar?: ").strip().lower()
    
    # Verifica se o comando está registrado nos aprendizados
    if comando in aprendizados:
        print("🤖", aprendizados[comando])
    else:
        print("❌ Eu ainda não aprendi isso.")

# Função para exibir todos os aprendizados
def ver_aprendizados():
    """
    Exibe todos os comandos e suas respostas armazenadas no arquivo de aprendizados.
    """
    aprendizados = carregar_aprendizados()
    
    if aprendizados:
        print("📚 Comandos aprendidos:")
        # Exibe cada comando e a resposta associada
        for chave, valor in aprendizados.items():
            print(f"• {chave} => {valor}")
    else:
        print("😕 Ainda não aprendi nada.")

# Função para conversar com o sistema
def conversar():
    """
    Permite uma conversa livre com o sistema. O usuário pode digitar comandos que
    foram ensinados ou digitar 'sair' para encerrar a conversa.
    """
    aprendizados = carregar_aprendizados()
    print("💬 Vamos conversar! (digite 'sair' para encerrar a conversa)\n")
    
    while True:
        entrada = input("👤 Você: ").strip().lower()
        
        # Encerra a conversa se o usuário digitar 'sair'
        if entrada == "sair":
            print("👋 Até logo!")
            break
        
        # Verifica se a entrada do usuário está registrada
        resposta = aprendizados.get(entrada, "🤖 Ainda não aprendi isso.")
        print("🤖 Egregoro:", resposta)

# Função principal do programa, que exibe o menu e executa as opções do usuário
def menu():
    """
    Exibe o menu principal com as opções disponíveis e executa a ação escolhida pelo usuário.
    """
    while True:
        print("\n===== 🌐 Egregoro IA =====")
        print("1. Ensinar comando")
        print("2. Executar comando")
        print("3. Ver aprendizados")
        print("4. Conversar livremente")
        print("5. Sair")

        # Solicita a escolha do usuário
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            ensinar()
        elif escolha == "2":
            executar()
        elif escolha == "3":
            ver_aprendizados()
        elif escolha == "4":
            conversar()
        elif escolha == "5":
            print("🛑 Encerrando Egregoro...")
            break
        else:
            print("❗ Opção inválida. Tente novamente.")

# Execução do programa
if __name__ == "__main__":
    atualizar_repositorio()  # Atualiza o repositório antes de iniciar
    menu()  # Inicia o menu do sistema
import os
import json
import subprocess
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Caminho para o arquivo de aprendizados
ARQUIVO_APRENDIZADO = os.getenv('ARQUIVO_APRENDIZADO', 'Aprendizados.json')

# Adicionar o diretório atual ao sys.path para garantir que o Python encontre os pacotes locais
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Importação do módulo executar de egos
from egos.executar import executar

def atualizar_repositorio():
    print("🔄 Verificando atualizações no repositório Git...")
    try:
        resultado = subprocess.run(["git", "pull"], cwd=os.path.dirname(__file__), capture_output=True, text=True)
        print(resultado.stdout)
        if "Already up to date." not in resultado.stdout:
            print("✅ Repositório atualizado com sucesso.")
        else:
            print("🟢 Já está na versão mais recente.")
    except Exception as e:
        print("⚠️ Erro ao atualizar o repositório:", str(e))

def carregar_aprendizados():
    """
    Função para carregar os aprendizados de um arquivo JSON.
    Retorna um dicionário de aprendizados ou um dicionário vazio se o arquivo não existir.
    """
    if os.path.exists(ARQUIVO_APRENDIZADO):
        with open(ARQUIVO_APRENDIZADO, 'r') as f:
            return json.load(f)
    return {}

def salvar_aprendizados(aprendizados):
    """
    Função para salvar os aprendizados em um arquivo JSON.
    """
    with open(ARQUIVO_APRENDIZADO, 'w') as f:
        json.dump(aprendizados, f, indent=4)

def ensinar():
    """
    Função para ensinar um novo comando e sua resposta.
    """
    aprendizados = carregar_aprendizados()
    chave = input("🧠 Digite o comando que você quer ensinar: ").strip()
    resposta = input("🗣️ E qual é a resposta que devo dar?: ").strip()
    aprendizados[chave.lower()] = resposta
    salvar_aprendizados(aprendizados)
    print("✅ Comando aprendido com sucesso!")

def executar_comando():
    """
    Função para executar um comando baseado nos aprendizados.
    """
    aprendizados = carregar_aprendizados()
    comando = input("🔎 O que deseja executar?: ").strip().lower()
    if comando in aprendizados:
        print("🤖", aprendizados[comando])
    else:
        print("❌ Eu ainda não aprendi isso.")

def ver_aprendizados():
    """
    Função para ver todos os aprendizados salvos.
    """
    aprendizados = carregar_aprendizados()
    if aprendizados:
        print("📚 Comandos aprendidos:")
        for chave, valor in aprendizados.items():
            print(f"• {chave} => {valor}")
    else:
        print("😕 Ainda não aprendi nada.")

def conversar():
    """
    Função para conversar com o sistema.
    O sistema responde com base nos comandos aprendidos.
    """
    aprendizados = carregar_aprendizados()
    print("💬 Vamos conversar! (digite 'sair' para encerrar a conversa)\n")
    while True:
        entrada = input("👤 Você: ").strip().lower()
        if entrada == "sair":
            print("👋 Até logo!")
            break
        resposta = aprendizados.get(entrada, "🤖 Ainda não aprendi isso.")
        print("🤖 Egregoro:", resposta)

def menu():
    """
    Função para exibir o menu de opções para o usuário.
    """
    while True:
        print("\n===== 🌐 Egregoro IA =====")
        print("1. Ensinar comando")
        print("2. Executar comando")
        print("3. Ver aprendizados")
        print("4. Conversar livremente")
        print("5. Sair")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            ensinar()
        elif escolha == "2":
            executar_comando()
        elif escolha == "3":
            ver_aprendizados()
        elif escolha == "4":
            conversar()
        elif escolha == "5":
            print("🛑 Encerrando Egregoro...")
            break
        else:
            print("❗ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    atualizar_repositorio()
    menu()

import os
import sys
from datetime import datetime

def executar_comando(comando: str) -> str:
    try:
        resultado = os.popen(comando).read()
        return resultado.strip() or "Comando executado sem saída."
    except Exception as e:
        return f"Erro ao executar: {str(e)}"

def criar_commit_versao(tag, mensagem):
    try:
        os.system("git add .")
        print("✅ Arquivos adicionados ao Git.")

        os.system(f'git commit -m "{mensagem}"')
        print("✅ Commit criado.")

        os.system(f'git tag {tag}')
        print(f"✅ Tag de versão '{tag}' criada.")

        print("✅ Commit local criado. Use 'git push' e 'git push --tags' para enviar ao GitHub.")

    except Exception as e:
        print(f"❌ Erro ao criar commit: {e}")

def main():
    if len(sys.argv) < 3:
        print("❌ Uso correto: python egregoro_main.py <versao_ex: v1_0_0> \"Mensagem do commit\"")
        return

    versao = sys.argv[1]
    mensagem = sys.argv[2]

    print(f"\n🚀 Iniciando nova versão: {versao}")
    print(f"📝 Mensagem: {mensagem}")
    print(f"🕒 Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    criar_commit_versao(versao, mensagem)

if __name__ == "__main__":
    main()
print("Egregoro - Versão de Teste v1.3.0")
import os
import json
from datetime import datetime

ARQUIVO_APRENDIZADO = "aprendizados.json"

class Egregoro:
    def __init__(self):
        self.aprendizados = []
        self.carregar_aprendizados()

    def carregar_aprendizados(self):
        if os.path.exists(ARQUIVO_APRENDIZADO):
            with open(ARQUIVO_APRENDIZADO, "r", encoding="utf-8") as f:
                self.aprendizados = json.load(f)
        else:
            self.aprendizados = []

    def salvar_aprendizados(self):
        with open(ARQUIVO_APRENDIZADO, "w", encoding="utf-8") as f:
            json.dump(self.aprendizados, f, indent=4, ensure_ascii=False)

    def aprender(self, informacao: str):
        registro = {
            "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "conteudo": informacao.strip()
        }
        self.aprendizados.append(registro)
        self.salvar_aprendizados()
        print(f"[+] Aprendido: {informacao}")

    def executar(self, comando: str):
        try:
            resultado = os.popen(comando).read()
            print(f"[Executando]: {comando}")
            print(resultado)
        except Exception as e:
            print(f"[Erro]: {str(e)}")

    def mostrar_aprendizados(self):
        print("\n📚 Egregoro - Aprendizados Registrados:")
        if not self.aprendizados:
            print("Nenhum aprendizado ainda.")
        else:
            for item in self.aprendizados:
                print(f"[{item['data_hora']}] → {item['conteudo']}")

# Interface simples
if __name__ == "__main__":
    egregoro = Egregoro()

    while True:
        print("\nEscolha uma opção:")
        print("1. Ensinar algo à Egregoro")
        print("2. Executar comando")
        print("3. Ver aprendizados")
        print("4. Sair")

        opcao = input("Opção: ").strip()

        if opcao == "1":
            info = input("Digite o que deseja ensinar: ")
            egregoro.aprender(info)

        elif opcao == "2":
            comando = input("Digite o comando para executar: ")
            egregoro.executar(comando)

        elif opcao == "3":
            egregoro.mostrar_aprendizados()

        elif opcao == "4":
            print("Encerrando a Egregoro...")
            break

        else:
            print("Opção inválida. Tente novamente.")

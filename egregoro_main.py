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

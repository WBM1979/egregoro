# egregoro_main.py

from egregoro.egos.ensinar import ensinar
from egregoro.egos.ver import ver
from egregoro.egos.executar import executar
from egregoro.egos.conversar import conversar

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



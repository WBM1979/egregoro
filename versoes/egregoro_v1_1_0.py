import os

class EgoExecutor:
    def executar_comando(self, comando: str) -> str:
        try:
            resultado = os.popen(comando).read()
            return resultado.strip() or "Comando executado sem saída."
        except Exception as e:
            return f"Erro ao executar: {str(e)}"

if __name__ == "__main__":
    ego = EgoExecutor()
    while True:
        entrada = input("Você: ")
        if entrada.lower() in ["sair", "exit", "quit"]:
            break
        if entrada.startswith("executar:"):
            comando = entrada.replace("executar:", "").strip()
            resposta = ego.executar_comando(comando)
            print("Egregoro:", resposta)
        else:
            print("Egregoro: Comando não reconhecido. Use 'executar: COMANDO'.")

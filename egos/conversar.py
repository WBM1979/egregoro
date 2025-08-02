def executar():
    print("🗣️ Iniciando conversa livre com a Egregoro. (Digite 'sair' para encerrar)")
    while True:
        entrada = input("Você: ")
        if entrada.lower() == 'sair':
            print("Egregoro: Até mais!")
            break
        resposta = f"Egregoro: Estou refletindo sobre isso: '{entrada}'"
        print(resposta)

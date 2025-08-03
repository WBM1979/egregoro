

def ensinar():
    print("Função ensinar executada")
def executar():
    dado = input("📚 O que deseja ensinar à Egregoro? ")
    if dado.strip():
        print(f"[Ensinar] Aprendizado registrado: {dado}")
    else:
        print("[Ensinar] Nenhum dado fornecido.")

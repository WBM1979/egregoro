# core/superego.py

from core.falangem import Falangem

class Superego:
    """
    Representa um Superego, que é uma união de várias falanges.
    Ele pode tomar decisões mais complexas, baseadas nas falanges que o compõem.
    """
    def __init__(self, nome: str):
        """
        Inicializa um Superego com um nome e uma lista vazia de falanges.
        """
        self.nome = nome
        self.falangens = []

    def adicionar_falangen(self, falangem: Falangem):
        """
        Adiciona uma falangem ao Superego, formando uma união de falanges.
        """
        self.falangens.append(falangem)

    def votar(self, proposta: str):
        """
        O Superego realiza uma votação somando os votos das falanges que ele contém.
        """
        votos_totais = 0
        for falangem in self.falangens:
            votos_totais += falangem.votar(proposta)
        return votos_totais

    def contar_falanges(self):
        """
        Retorna o número de falanges que o Superego contém.
        """
        return len(self.falangens)

    def __str__(self):
        """
        Retorna uma representação do Superego, listando as falanges que ele contém.
        """
        falangens_nomes = [f.nome for f in self.falangens]
        return f"Superego(nome={self.nome}, falanges={falangens_nomes})"

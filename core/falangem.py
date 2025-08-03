
# core/falangem.py

from core.ego import Ego

class Falangem:
    """
    Representa um grupo de egos com especialidades similares que trabalham juntos para resolver problemas.
    """
    def __init__(self, nome: str, especialidade: str):
        self.nome = nome
        self.especialidade = especialidade
        self.egos = []

    def adicionar_ego(self, ego: Ego):
        """
        Adiciona um Ego à falangem se ele tiver a mesma especialidade.
        """
        if ego.especialidade == self.especialidade:
            self.egos.append(ego)
        else:
            raise ValueError(f"Ego com especialidade '{ego.especialidade}' não pode ser adicionado à falangem de '{self.especialidade}'.")

    def contar_egos(self):
        """
        Retorna o número de egos na falangem.
        """
        return len(self.egos)

    def votar(self, proposta: str):
        """
        Cada ego da falangem 'vota' em uma proposta.
        A lógica é simbólica e retorna a contagem de votos favoráveis.
        """
        votos = 0
        for ego in self.egos:
            # Simulação simples: todos egos ativos aceitam a proposta
            if ego.status == "ativo":
                votos += 1
        return votos

    def __str__(self):
        return f"Falangem(nome={self.nome}, especialidade={self.especialidade}, egos={[e.nome for e in self.egos]})"

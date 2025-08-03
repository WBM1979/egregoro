# core/ego.py

class Ego:
    def __init__(self, nome, especialidade, status="ativo"):
        """
        Inicializa um novo Ego com nome, especialidade e status padrão "ativo".
        """
        self.nome = nome
        self.especialidade = especialidade
        self.status = status  # ← foi adicionado para corrigir o erro do teste
        self.conexoes = []  # lista de conexões com outros egos

    def adicionar_conexao(self, outro_ego):
        """
        Adiciona outro Ego à lista de conexões se ainda não estiver conectado.
        """
        if outro_ego not in self.conexoes:
            self.conexoes.append(outro_ego)

    def __str__(self):
        """
        Retorna uma representação em string do Ego com nome, especialidade, status e conexões.
        """
        conexoes_nomes = [ego.nome for ego in self.conexoes]
        return f"Ego(nome={self.nome}, especialidade={self.especialidade}, status={self.status}, conexoes={conexoes_nomes})"

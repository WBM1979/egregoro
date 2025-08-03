import unittest
from core.ego import Ego  # Importa a classe Ego do módulo core.ego

class TestEgo(unittest.TestCase):
    """
    Testes unitários para a classe Ego definida em core/ego.py
    """

    def test_criacao_do_ego(self):
        """
        Testa se o Ego é criado corretamente com os atributos fornecidos.
        """
        ego = Ego(nome="Ego1", especialidade="matemática")
        self.assertEqual(ego.nome, "Ego1")
        self.assertEqual(ego.especialidade, "matemática")
        self.assertEqual(ego.status, "ativo")  # valor padrão
        self.assertEqual(ego.conexoes, [])     # valor padrão

    def test_adicionar_conexao(self):
        """
        Testa se um ego pode adicionar outro ego como conexão.
        """
        ego1 = Ego(nome="Ego1", especialidade="visão")
        ego2 = Ego(nome="Ego2", especialidade="fala")

        ego1.adicionar_conexao(ego2)

        self.assertIn(ego2, ego1.conexoes)
        self.assertEqual(len(ego1.conexoes), 1)

    def test_representacao_em_string(self):
        """
        Testa se a representação em string do Ego está correta.
        """
        ego = Ego(nome="EgoTeste", especialidade="memória")
        representacao = str(ego)
        self.assertIn("EgoTeste", representacao)
        self.assertIn("memória", representacao)
        self.assertIn("ativo", representacao)

if __name__ == '__main__':
    unittest.main()

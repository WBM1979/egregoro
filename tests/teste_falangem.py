# tests/teste_falangem.py

import unittest
from core.ego import Ego
from core.falangem import Falangem

class TestFalangem(unittest.TestCase):

    def test_criacao_falangem(self):
        falange = Falangem(nome="MemoriaFalange", especialidade="memória")
        self.assertEqual(falange.nome, "MemoriaFalange")
        self.assertEqual(falange.especialidade, "memória")
        self.assertEqual(falange.contar_egos(), 0)

    def test_adicionar_ego(self):
        falange = Falangem(nome="VisaoFalange", especialidade="visão")
        ego1 = Ego(nome="Ego1", especialidade="visão")
        falange.adicionar_ego(ego1)
        self.assertEqual(falange.contar_egos(), 1)

    def test_adicionar_ego_com_especialidade_errada(self):
        falange = Falangem(nome="FalangeRaciocinio", especialidade="lógica")
        ego_errado = Ego(nome="Errado", especialidade="visão")
        with self.assertRaises(ValueError):
            falange.adicionar_ego(ego_errado)

    def test_votacao(self):
        falange = Falangem(nome="DecisaoFalange", especialidade="decisão")
        for i in range(3):
            ego = Ego(nome=f"Ego{i}", especialidade="decisão")
            falange.adicionar_ego(ego)
        votos = falange.votar("Proposta X")
        self.assertEqual(votos, 3)

if __name__ == '__main__':
    unittest.main()

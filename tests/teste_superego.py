# tests/teste_superego.py

import unittest
from core.ego import Ego
from core.falangem import Falangem
from core.superego import Superego

class TestSuperego(unittest.TestCase):

    def test_criacao_superego(self):
        superego = Superego(nome="SuperDecisao")
        self.assertEqual(superego.nome, "SuperDecisao")
        self.assertEqual(superego.contar_falanges(), 0)

    def test_adicionar_falangem(self):
        superego = Superego(nome="SuperMemoria")
        falangem = Falangem(nome="FalangeMemoria", especialidade="memória")
        superego.adicionar_falangen(falangem)
        self.assertEqual(superego.contar_falanges(), 1)

    def test_votacao_superego(self):
        superego = Superego(nome="SuperDecisao")
        falangem1 = Falangem(nome="FalangeVisao", especialidade="visão")
        falangem2 = Falangem(nome="FalangeLinguistica", especialidade="linguística")

        ego1 = Ego(nome="Ego1", especialidade="visão")
        ego2 = Ego(nome="Ego2", especialidade="linguística")

        falangem1.adicionar_ego(ego1)
        falangem2.adicionar_ego(ego2)

        superego.adicionar_falangen(falangem1)
        superego.adicionar_falangen(falangem2)

        votos = superego.votar("Proposta Y")
        self.assertEqual(votos, 2)  # Voto de 2 egos, um de cada falangem

if __name__ == '__main__':
    unittest.main()

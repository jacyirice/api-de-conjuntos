import unittest
from conjuntos import Conjunto

class ConjuntoTest(unittest.TestCase):

    # tamanho
    def test_tamanho(self):
        A = Conjunto(1, 2, 3, 4, 5)
        self.assertEqual(A.tamanho(), 5)

    # possui
    def test_possui(self):
        A = Conjunto(1, 2, 3, 4)
        self.assertTrue(A.possui(3))

    def test_nao_possui(self):
        A = Conjunto(1, 2, 3, 4)
        self.assertFalse(A.possui(10))

    def test_possui_conjunto(self):
        A = Conjunto(1, 2, 3, 4)
        B = Conjunto(1, 2, A)
        self.assertTrue(B.possui(A))

    # contem
    def test_contem(self):
        A = Conjunto(1, 2)
        B = Conjunto(1, 2, 3, 4)
        self.assertTrue(B.contem(A))

    def test_contem_igual(self):
        A = Conjunto(1, 2)
        self.assertTrue(A.contem(A))

    def test_nao_contem(self):
        A = Conjunto(1, 2)
        C = Conjunto(5, 6, 7)
        self.assertFalse(C.contem(A))

    # contem_propriamente
    def test_contem_propriamente(self):
        A = Conjunto(1, 2, 3)
        B = Conjunto(1, 2)
        self.assertTrue(A.contem_propriamente(B))

    def test_contem_propriamente_igual(self):
        A = Conjunto(1, 2, 3)
        B = Conjunto(1, 2)
        self.assertFalse(A.contem_propriamente(A))

    def test_nao_contem_propriamente(self):
        A = Conjunto(1, 2, 3)
        B = Conjunto(1, 2)
        self.assertFalse(B.contem_propriamente(A))

    # eh_igual
    def test_eh_igual(self):
        A = Conjunto(1, 2)
        B = Conjunto(1, 2)
        self.assertTrue(A.eh_igual(B))

    def test_nao_eh_igual(self):
        A = Conjunto(1, 2)
        C = Conjunto(1, 2, 3)
        self.assertFalse(A.eh_igual(C))

    # eh_vazio
    def test_eh_vazio(self):
        B = Conjunto()
        self.assertTrue(B.eh_vazio())

    def test_nao_eh_vazio(self):
        A = Conjunto(1, 2, 3)
        self.assertFalse(A.eh_vazio())

    # uniao
    def test_uniao(self):
        A = Conjunto(1, 2)
        B = Conjunto(1, 2, 3)
        C = Conjunto(1, 2, 3)
        self.assertEqual(A.uniao(B).elementos, C.elementos)

    def test_nao_uniao(self):
        A = Conjunto(1, 2)
        B = Conjunto(1, 2, 3)
        C = Conjunto(1, 2, 3, 4)
        self.assertNotEqual(A.uniao(B).elementos, C.elementos)

    # intersecçao
    def test_interseccao(self):
        A = Conjunto(1, 2)
        B = Conjunto(2, 3, 4)
        C = A.intersecao(B)
        self.assertEqual(C.elementos, Conjunto(2).elementos)

    # diferença
    def test_diferenca(self):
        A = Conjunto(1, 2, 3)
        B = Conjunto(1, 4)
        C = A.diferenca(B)
        self.assertEqual(C.elementos, Conjunto(2, 3).elementos)

    # complemento
    def test_complemento(self):
        U = Conjunto(1, 2, 3, 4, 5)
        A = Conjunto(1, 2)
        C = A.complemento(U)
        self.assertEqual(C.elementos, Conjunto(3, 4, 5).elementos)

    # conjunto das partes
    def test_conjunto_das_partes(self):
        A = Conjunto(1, 2, 3)
        P = A.conjunto_das_partes()
        R = Conjunto(
            Conjunto(), Conjunto(1), Conjunto(2), Conjunto(3),
            Conjunto(1, 2), Conjunto(1, 3), Conjunto(2, 3),
            Conjunto(1, 2, 3)
        )
        self.assertEqual(str(P), str(R))

    # produto cartesiano
    def test_produto_cartesiano(self):
        A = Conjunto(1, 2, 3)
        B = Conjunto(4, 5, 6)
        P = A.produto_cartesiano(B)
        R = Conjunto(
            (1, 4), (1, 5), (1, 6),
            (2, 4), (2, 5), (2, 6),
            (3, 4), (3, 5), (3, 6)
        )
        self.assertEqual(P.elementos, R.elementos)

    # string
    def test_string(self):
        A = Conjunto(1, 2, 3)
        B = Conjunto(1, A)
        C = Conjunto()
        D = Conjunto(A, B, C)
        R = '{{1, 2, 3}, {1, {1, 2, 3}}, {}}'
        self.assertEqual(D.string(), R)

if __name__ == '__main__':
    unittest.main()

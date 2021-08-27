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

    def test_intersecçao(self):
        A = Conjunto(1, 2)
        B = Conjunto(2, 3, 4)
        C = A.intersecao(B)
        self.assertEqual(C.elementos, Conjunto(2).elementos)

    def test_diferenca(self):
        A = Conjunto(1, 2, 3)
        B = Conjunto(1, 4)
        C = A.diferenca(B)
        self.assertEqual(C.elementos, Conjunto(2, 3).elementos)


if __name__ == '__main__':
    unittest.main()

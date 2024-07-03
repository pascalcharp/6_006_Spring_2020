import unittest
from lib.ListeSimplementChainee import ListeSimplementChainee

class TestsListeSimplementChainee(unittest.TestCase):
    def setUp(self) -> None:
        self.vide = ListeSimplementChainee()
        self.l1 = ListeSimplementChainee([1])
        self.l5 = ListeSimplementChainee([1, 2, 3, 4, 5])

    def test_construction(self):
        self.assertEqual("[]", self.vide.__str__())
        self.assertEqual("[1]", self.l1.__str__())
        self.assertEqual("[1, 2, 3, 4, 5]", self.l5.__str__())

    def test_inserer_premier_vide(self):
        self.vide.inserer_premier(42)
        self.assertEqual("[42]", self.vide.__str__())

    def test_inserer_premier_l1(self):
        self.l1.inserer_premier(42)
        self.assertEqual("[42, 1]", self.l1.__str__())

    def test_inserer_premier_l5(self):
        self.l5.inserer_premier(42)
        self.assertEqual("[42, 1, 2, 3, 4, 5]", self.l5.__str__())

    def test_retirer_premier_l1(self):
        self.assertEqual(1, self.l1.retirer_premier())
        self.assertEqual("[]", self.l1.__str__())

    def test_retirer_premier_l5(self):
        self.assertEqual(1, self.l5.retirer_premier())
        self.assertEqual("[2, 3, 4, 5]", self.l5.__str__())

    def test_lire_dernier_l1(self):
        self.assertEqual(1, self.l1.lire_dernier())

    def test_inserer_dernier(self):
        self.vide.inserer_dernier(42)
        self.assertEqual("[42]", self.vide.__str__())

    def test_inserer_dernier_l1(self):
        self.l1.inserer_dernier(42)
        self.assertEqual("[1, 42]", self.l1.__str__())

    def test_inserer_dernier_l5(self):
        self.l5.inserer_dernier(42)
        self.assertEqual("[1, 2, 3, 4, 5, 42]", self.l5.__str__())

    def test_retirer_dernier_l1(self):
        self.assertEqual(1, self.l1.retirer_dernier())
        self.assertEqual("[]", self.l1.__str__())

    def test_retirer_dernier_l5(self):
        self.assertEqual(5, self.l5.retirer_dernier())
        self.assertEqual("[1, 2, 3, 4]", self.l5.__str__())

    def test_inserer_index_l1_0(self):
        self.l1.inserer_index(0, 42)
        self.assertEqual("[42, 1]", self.l1.__str__())

    def test_inserer_index_l1_1(self):
        self.l1.inserer_index(1, 42)
        self.assertEqual("[1, 42]", self.l1.__str__())

    def test_inserer_index_l5_2(self):
        self.l5.inserer_index(2, 42)
        self.assertEqual("[1, 2, 42, 3, 4, 5]", self.l5.__str__())



if __name__ == "__main__":
    unittest.main()
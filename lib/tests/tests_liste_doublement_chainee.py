import unittest
from lib.ListeDoublementChainee import ListeDoublementChainee


class TestsListeDoublementChainee(unittest.TestCase):
    def setUp(self) -> None:
        self.liste_vide = ListeDoublementChainee()
        self.l1 = ListeDoublementChainee([1])
        self.l5 = ListeDoublementChainee([1, 2, 3, 4, 5])

    def test_construction_liste_vide(self):
        self.assertEqual("[]", self.liste_vide.__str__())
        self.assertEqual(0, len(self.liste_vide))

    def test_construction_liste_un_element(self):
        self.assertEqual("[1]", self.l1.__str__())
        self.assertEqual(1, len(self.l1))

    def test_construction_liste_cinq_elements(self):
        self.assertEqual("[1, 2, 3, 4, 5]", self.l5.__str__())
        self.assertEqual(5, len(self.l5))

    def test_iteration_liste_cinq_elements(self):
        i = 1
        for e in self.l5:
            self.assertEqual(i, e)
            i += 1

    def test_inserer_premier_liste_vide(self):
        self.liste_vide.inserer_premier(42)
        self.assertEqual("[42]", self.liste_vide.__str__())

    def test_inserer_dernier_liste_vide(self):
        self.liste_vide.inserer_dernier(42)
        self.assertEqual("[42]", self.liste_vide.__str__())

    def test_inserer_premier_l1(self):
        self.l1.inserer_premier(42)
        self.assertEqual("[42, 1]", self.l1.__str__())

    def test_inserer_dernier_l1(self):
        self.l1.inserer_dernier(42)
        self.assertEqual("[1, 42]", self.l1.__str__())

    def test_inserer_premier_l5(self):
        self.l5.inserer_premier(42)
        self.assertEqual("[42, 1, 2, 3, 4, 5]", self.l5.__str__())

    def test_inserer_dernier_l5(self):
        self.l5.inserer_dernier(42)
        self.assertEqual("[1, 2, 3, 4, 5, 42]", self.l5.__str__())

    def test_inserer_index_l5_position_0(self):
        self.l5.inserer_index(0, 42)
        self.assertEqual("[42, 1, 2, 3, 4, 5]", self.l5.__str__())

    def test_inserer_index_l5_position_1(self):
        self.l5.inserer_index(1, 42)
        self.assertEqual("[1, 42, 2, 3, 4, 5]", self.l5.__str__())

    def test_inserer_index_l5_position_2(self):
        self.l5.inserer_index(2, 42)
        self.assertEqual("[1, 2, 42, 3, 4, 5]", self.l5.__str__())

    def test_inserer_index_l5_position_3(self):
        self.l5.inserer_index(3, 42)
        self.assertEqual("[1, 2, 3, 42, 4, 5]", self.l5.__str__())

    def test_inserer_index_l5_position_4(self):
        self.l5.inserer_index(4, 42)
        self.assertEqual("[1, 2, 3, 4, 42, 5]", self.l5.__str__())

    def test_inserer_index_l5_position_5(self):
        self.l5.inserer_index(5, 42)
        self.assertEqual("[1, 2, 3, 4, 5, 42]", self.l5.__str__())

    def test_retirer_premier_l1(self):
        self.assertEqual(1, self.l1.retirer_premier())
        self.assertEqual("[]", self.l1.__str__())

    def test_retirer_dernier_l1(self):
        self.assertEqual(1, self.l1.retirer_dernier())
        self.assertEqual("[]", self.l1.__str__())

    def test_retirer_index_l5_position_0(self):
        self.assertEqual(1, self.l5.retirer_index(0))
        self.assertEqual("[2, 3, 4, 5]", self.l5.__str__())

    def test_retirer_index_l5_position_1(self):
        self.assertEqual(2, self.l5.retirer_index(1))
        self.assertEqual("[1, 3, 4, 5]", self.l5.__str__())

    def test_lire_index_l5_position(self):
        for i in range(5):
            self.assertEqual(i+1, self.l5[i])


if __name__ == '__main__':
    unittest.main()

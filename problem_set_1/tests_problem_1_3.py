import unittest
from problem_1_3 import VecteurDouble


class TestVecteurDouble(unittest.TestCase):
    def setUp(self) -> None:
        self.vide = VecteurDouble()
        self.dv1 = VecteurDouble([1])
        self.dv2 = VecteurDouble([1, 2])
        self.dv7 = VecteurDouble([1, 2, 3, 4, 5, 6, 7])

    def test_str(self):
        self.assertEqual("[]", self.vide.__str__())
        self.assertEqual("[1]", self.dv1.__str__())
        self.assertEqual("[1, 2]", self.dv2.__str__())
        self.assertEqual("[1, 2, 3, 4, 5, 6, 7]", self.dv7.__str__())

    def test_inserer_premier(self):
        self.vide.inserer_premier(42)
        self.assertEqual("[42]", self.vide.__str__())
        self.assertEqual(1, len(self.vide))
        self.dv1.inserer_premier(42)
        self.assertEqual("[42, 1]", self.dv1.__str__())
        self.assertEqual(2, len(self.dv1))
        self.dv2.inserer_premier(42)
        self.assertEqual("[42, 1, 2]", self.dv2.__str__())
        self.assertEqual(3, len(self.dv2))
        self.dv7.inserer_premier(42)
        self.assertEqual("[42, 1, 2, 3, 4, 5, 6, 7]", self.dv7.__str__())
        self.assertEqual(8, len(self.dv7))

    def test_inserer_dernier(self):
        self.vide.inserer_dernier(42)
        self.assertEqual("[42]", self.vide.__str__())
        self.assertEqual(1, len(self.vide))
        self.dv1.inserer_dernier(42)
        self.assertEqual("[1, 42]", self.dv1.__str__())
        self.assertEqual(2, len(self.dv1))
        self.dv2.inserer_dernier(42)
        self.assertEqual("[1, 2, 42]", self.dv2.__str__())
        self.assertEqual(3, len(self.dv2))

    def test_retirer_premier(self):
        self.assertEqual(1, self.dv1.retirer_premier())
        self.assertEqual("[]", self.dv1.__str__())
        self.assertEqual(0, len(self.dv1))
        self.assertEqual(1, self.dv2.retirer_premier())
        self.assertEqual("[2]", self.dv2.__str__())
        self.assertEqual(1, len(self.dv2))
        self.assertEqual(1, self.dv7.retirer_premier())
        self.assertEqual("[2, 3, 4, 5, 6, 7]", self.dv7.__str__())
        self.assertEqual(6, len(self.dv7))

    def test_retirer_dernier(self):
        self.assertEqual(1, self.dv1.retirer_dernier())
        self.assertEqual("[]", self.dv1.__str__())
        self.assertEqual(0, len(self.dv1))
        self.assertEqual(2, self.dv2.retirer_dernier())
        self.assertEqual("[1]", self.dv2.__str__())
        self.assertEqual(1, len(self.dv2))
        self.assertEqual(7, self.dv7.retirer_dernier())
        self.assertEqual("[1, 2, 3, 4, 5, 6]", self.dv7.__str__())
        self.assertEqual(6, len(self.dv7))

    def test_inserer_index_dv7_0(self):
        self.dv7.inserer_index(0, 42)
        self.assertEqual("[42, 1, 2, 3, 4, 5, 6, 7]", self.dv7.__str__())
        self.assertEqual(8, len(self.dv7))

    def test_inserer_index_dv7_1(self):
        self.dv7.inserer_index(1, 42)
        self.assertEqual("[1, 42, 2, 3, 4, 5, 6, 7]", self.dv7.__str__())
        self.assertEqual(8, len(self.dv7))

    def test_inserer_index_dv7_2(self):
        self.dv7.inserer_index(2, 42)
        self.assertEqual("[1, 2, 42, 3, 4, 5, 6, 7]", self.dv7.__str__())
        self.assertEqual(8, len(self.dv7))

    def test_inserer_dv7_7(self):
        self.dv7.inserer_index(7, 42)
        self.assertEqual("[1, 2, 3, 4, 5, 6, 7, 42]", self.dv7.__str__())
        self.assertEqual(8, len(self.dv7))

    def test_retirer_index_dv1_0(self):
        self.assertEqual(1, self.dv1.retirer_index(0))
        self.assertEqual("[]", self.dv1.__str__())
        self.assertEqual(0, len(self.dv1))

    def test_retirer_index_dev2_1(self):
        self.assertEqual(2, self.dv2.retirer_index(1))
        self.assertEqual("[1]", self.dv2.__str__())
        self.assertEqual(1, len(self.dv2))

    def test_retirer_index_dv2_0(self):
        self.assertEqual(1, self.dv2.retirer_index(0))
        self.assertEqual("[2]", self.dv2.__str__())
        self.assertEqual(1, len(self.dv2))

    def test_retirer_index_dv7_0(self):
        self.assertEqual(1, self.dv7.retirer_index(0))
        self.assertEqual("[2, 3, 4, 5, 6, 7]", self.dv7.__str__())
        self.assertEqual(6, len(self.dv7))

    def test_retraits_repetes_dv7(self):
        self.assertEqual(1, self.dv7.retirer_premier())
        self.assertEqual(2, self.dv7.retirer_premier())
        self.assertEqual(3, self.dv7.retirer_premier())
        self.assertEqual("[4, 5, 6, 7]", self.dv7.__str__())
        self.assertEqual(7, self.dv7.retirer_dernier())
        self.assertEqual(6, self.dv7.retirer_dernier())
        self.assertEqual("[4, 5]", self.dv7.__str__())
        self.assertEqual(5, self.dv7.retirer_dernier())
        self.assertEqual("[4]", self.dv7.__str__())
        self.assertEqual(4, self.dv7.retirer_dernier())



if __name__ == '__main__':
    unittest.main()

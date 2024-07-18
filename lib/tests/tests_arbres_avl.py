import unittest
from lib.ArbreBinaireAVL import ArbreBinaireAVL


class TestArbreBinaireAVL(unittest.TestCase):
    def setUp(self):
        self.cles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        self.val = [cle * 10 for cle in self.cles]
        paires = [(cle, cle * 10) for cle in self.cles]
        self.arbre = ArbreBinaireAVL(paires)

    def test_init(self):
        self.assertEqual(10, len(self.arbre))
        observed_keys = [k for k, _ in self.arbre]
        observed_values = [v for _, v in self.arbre]
        self.assertEqual(self.cles, observed_keys)
        self.assertEqual(self.val, observed_values)

    def test_delete_one_element(self):
        self.arbre.delete(50)
        self.assertEqual(9, len(self.arbre))
        self.cles.remove(50)
        self.val.remove(500)
        observed_keys = [k for k, _ in self.arbre]
        observed_values = [v for _, v in self.arbre]
        self.assertEqual(self.cles, observed_keys)
        self.assertEqual(self.val, observed_values)

    def test_delete_two_consecutive_elements(self):
        self.arbre.delete(40)
        self.arbre.delete(50)
        self.assertEqual(8, len(self.arbre))
        self.cles.remove(50)
        self.val.remove(500)
        self.cles.remove(40)
        self.val.remove(400)
        observed_keys = [k for k, _ in self.arbre]
        observed_values = [v for _, v in self.arbre]
        self.assertEqual(self.cles, observed_keys)
        self.assertEqual(self.val, observed_values)

    def test_delete_all_elements(self):
        for cle in self.cles:
            self.arbre.delete(cle)
        self.assertEqual(0, len(self.arbre))


if __name__ == '__main__':
    unittest.main()

import unittest
from lib.ListeDoublementChainee import ListeDoublementChainee
from problem_1_2 import renverser, deplacer, deplacer_un_vers_la_droite, deplacer_un_vers_la_gauche


class TestDeplacer(unittest.TestCase):
    def setUp(self) -> None:
        self.L = ListeDoublementChainee([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_renverser(self):
        renverser(self.L, 2, 5)
        self.assertEqual("[1, 2, 7, 6, 5, 4, 3, 8, 9, 10]", self.L.__str__())

    def test_deplacer(self):
        deplacer(self.L, 2, 4, 8)
        self.assertEqual("[1, 2, 7, 8, 3, 4, 5, 6, 9, 10]", self.L.__str__())


if __name__ == '__main__':
    unittest.main()

import unittest
from lib.ListeDoublementChainee import ListeDoublementChainee


class TestProblem_1_4(unittest.TestCase):
    def setUp(self) -> None:
        self.l1 = ListeDoublementChainee([1, 2, 3, 4, 5])
        self.l2 = ListeDoublementChainee([6, 7, 8, 9, 10])

    def test_joindre(self):
        self.l1.joindre(self.l2)
        self.assertEqual("[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]", self.l1.__str__())
        self.assertEqual("[]", self.l2.__str__())

    def test_separer(self):
        res = self.l1.separer(1, 3)
        self.assertEqual("[1, 5]", self.l1.__str__())
        self.assertEqual("[2, 3, 4]", res.__str__())


if __name__ == '__main__':
    unittest.main()

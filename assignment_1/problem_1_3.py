from lib.ListeDoublementChainee import ListeDoublementChainee


class Binder(ListeDoublementChainee):
    def __init__(self, elements=None):
        super().__init__(elements)
        self.index = [e for e in self]
        self.bookmark = {"A": (self.__tete, 0), "B": (self.__queue, self.__cardinal)}

    def shift_mark(self, m, d):
        assert m in self.bookmark.keys()
        assert d in [-1, +1]

        if d == -1:
            self.bookmark[m][0] = self.bookmark[m][0].prev
        else:
            self.bookmark[m][0] = self.bookmark[m][0].next
        self.bookmark[m][1] += d

    def place_mark(self, i, m):
        assert m in self.bookmark.keys()
        assert i in range(self.__cardinal)

        if i > self.bookmark[m][1]:
            for _ in range(i - self.bookmark[m][1]):
                self.shift_mark(m, 1)
        else:
            for _ in range(self.bookmark[m][1] - i):
                self.shift_mark(m, -1)

        assert self.bookmark["A"][1] < self.bookmark["B"][1]

    def read_page(self, i):
        assert i in range(self.__cardinal)
        return self.index[i]

    def move_page(self, m):
        assert m in ["A", "B"]



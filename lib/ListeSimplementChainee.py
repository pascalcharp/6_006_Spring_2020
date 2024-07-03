from lib.sequence import Sequence

class _Element:
    def __init__(self, val):
        self.cle = val
        self.next = None


class ListeSimplementChainee(Sequence):
    def __init__(self, elements=None):
        self.__tete = None
        self.__cardinal = 0
        if elements is None:
            elements = []
        for e in reversed(elements):
            self.inserer_premier(e)
        assert self._invariant()

    def __len__(self):
        return self.__cardinal

    def __str__(self):
        resultat = "["
        s = self.__tete
        while s is not None:
            resultat += s.cle.__str__()
            s = s.next
            if s is not None:
                resultat += ", "
        resultat += "]"
        return resultat

    def lire_premier(self):
        return self.__tete.cle

    def inserer_premier(self, x):
        n = _Element(x)
        n.next = self.__tete
        self.__tete = n
        self.__cardinal += 1
        assert self._invariant()

    def retirer_premier(self):
        val = self.__tete.cle
        self.__tete = self.__tete.next
        self.__cardinal -= 1
        assert self._invariant()
        return val

    def lire_dernier(self):
        _, s = self._trouver_dernier()
        return s.cle


    def inserer_dernier(self, x):
        n = _Element(x)
        if self.__cardinal == 0:
            self.__tete = n
        else:
            _, s = self._trouver_dernier()
            s.next = n
        self.__cardinal += 1
        assert self._invariant()


    def retirer_dernier(self):
        if self.__cardinal == 1:
            return self.retirer_premier()
        else:
            p, s = self._trouver_dernier()
            val = s.cle
            p.next = None
        self.__cardinal -= 1
        assert self._invariant()
        return val

    def lire_index(self, n):
        _, s = self._trouver_index(n)
        return s.cle

    def inserer_index(self, n, x):
        if n == 0:
            self.inserer_premier(x)
        else:
            p, s = self._trouver_index(n)
            nouv = _Element(x)
            p.next = nouv
            nouv.next = s
            self.__cardinal += 1
            assert self._invariant()

    def retirer_index(self, n):
        if n == 0:
            return self.retirer_premier()
        p, s = self._trouver_index(n)
        p.next = s.next
        self.__cardinal -= 1
        assert self._invariant()
        return s.cle

    def _invariant(self):
        s = self.__tete
        for i in range(self.__cardinal):
            s = s.next
        return s is None

    def _trouver_index(self, n):
        s = self.__tete
        prev = None
        for i in range(n):
            prev = s
            s = s.next
        return prev, s

    def _trouver_dernier(self):
        return self._trouver_index(self.__cardinal - 1)

    def renverser_ordre(self):
        assert self.__cardinal > 3 and self.__cardinal % 2 == 0
        mid = self.__cardinal // 2
        end, cur = self._trouver_index(mid)
        suiv = cur.next
        cur.next = None
        while suiv is not None:
            suivsuiv = suiv.next
            suiv.next = cur
            cur = suiv
            suiv = suivsuiv
        end.next = cur
        assert self._invariant()



from lib.sequence import Sequence


class _Noeud:
    def __init__(self, val=None):
        self.cle = val
        self.next = None
        self.prev = None


class ListeDoublementChaineeIterateur:
    def __init__(self, premier, dernier):
        self._courant = premier
        self._dernier = dernier

    def __next__(self):
        self._courant = self._courant.next
        if self._courant == self._dernier:
            raise StopIteration
        return self._courant.cle


class ListeDoublementChainee(Sequence):
    def __init__(self, elements=None):
        self.__tete = _Noeud()
        self.__queue = _Noeud()
        self.__tete.next = self.__queue
        self.__queue.prev = self.__tete
        self.__cardinal = 0
        if elements is None:
            elements = []
        for elem in elements:
            self.inserer_dernier(elem)
        assert self.__invariant()

    def __iter__(self):
        return ListeDoublementChaineeIterateur(self.__tete, self.__queue)

    def __len__(self):
        return self.__cardinal

    def __getitem__(self, pos):
        return self.lire_index(pos)

    def __contains__(self, item):
        s = self.__tete.next
        for _ in range(len(self)):
            if s.cle == item:
                return True
        return False

    def __str__(self):
        res = "["
        s = self.__tete.next
        for i in range(self.__cardinal):
            res += s.cle.__str__()
            if i < self.__cardinal - 1:
                res += ", "
            s = s.next
        res += "]"
        return res

    def est_vide(self):
        return len(self) == 0

    def lire_premier(self):
        return self.__tete.next.cle

    def inserer_premier(self, x):
        n = _Noeud(x)
        self.__tete.next.prev = n
        n.next = self.__tete.next
        self.__tete.next = n
        n.prev = self.__tete
        self.__cardinal += 1
        assert self.__invariant()

    def retirer_premier(self):
        s = self.__tete.next
        val = s.cle
        s.next.prev = self.__tete
        self.__tete.next = s.next
        self.__cardinal -= 1
        assert self.__invariant()
        return val

    def lire_dernier(self):
        return self.__queue.prev.cle

    def inserer_dernier(self, x):
        n = _Noeud(x)
        self.__queue.prev.next = n
        n.prev = self.__queue.prev
        self.__queue.prev = n
        n.next = self.__queue
        self.__cardinal += 1
        assert self.__invariant()

    def retirer_dernier(self):
        s = self.__queue.prev
        val = s.cle
        s.prev.next = self.__queue
        self.__queue.prev = s.prev
        self.__cardinal -= 1
        assert self.__invariant()
        return val

    def lire_index(self, pos):
        return self.__trouver_noeud(pos).cle

    def inserer_index(self, pos, x):
        nouveau = _Noeud(x)
        c = self.__trouver_noeud(pos)
        c.prev.next = nouveau
        nouveau.prev = c.prev
        c.prev = nouveau
        nouveau.next = c
        self.__cardinal += 1
        assert self.__invariant()

    def retirer_index(self, pos):
        s = self.__trouver_noeud(pos)
        val = s.cle
        s.prev.next = s.next
        s.next.prev = s.prev
        self.__cardinal -= 1
        assert self.__invariant()
        return val

    def __trouver_noeud_par_la_tete(self, n):
        s = self.__tete.next
        for _ in range(n):
            s = s.next
        return s

    def __trouver_noeud_par_la_queue(self, n):
        s = self.__queue
        for _ in range(self.__cardinal - n):
            s = s.prev
        return s

    def __trouver_noeud(self, n):
        if n < self.__cardinal // 2:
            return self.__trouver_noeud_par_la_tete(n)
        else:
            return self.__trouver_noeud_par_la_queue(n)

    def __invariant(self):
        s = self.__tete.next
        for _ in range(self.__cardinal):
            s = s.next
        if s != self.__queue:
            return False
        s = self.__queue.prev
        for _ in range(self.__cardinal):
            s = s.prev
        return s == self.__tete

    def joindre(self, liste):
        while len(liste) > 0:
            self.inserer_dernier(liste.retirer_premier())

    def separer(self, i, j):
        retval = ListeDoublementChainee()
        for _ in range(j - i + 1):
            retval.inserer_dernier(self.retirer_index(i))
        return retval

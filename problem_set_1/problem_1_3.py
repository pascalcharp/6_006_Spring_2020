from lib.sequence import Sequence


class VecteurDouble(Sequence):
    """
    Structure de données permettant une insertion et retrait en O(1) aux deux extrémités.  Il s'agit essentiellement
    de deux vecteurs mis bout à bout.

    Lorsqu'un retrait d'élément conduit à vider complètement un des deux vecteurs, le conteneur est rééquilibré pour
    répartir les éléments environ également entre les deux vecteurs.  Lorsqu'un seul élément reste, il est stocké dans
    le vecteur de droite.
    """

    def __init__(self, elements=None):
        """
        Crée un conteneur à partir d'un itérable.
        :param elements: itérable contenant les éléments à stocker dans l'ordre
        """
        if elements is None:
            elements = []
        self.cardinal = len(elements)
        self.__lg = [x for x in reversed(elements[0: self.cardinal // 2])]
        self.__ld = [x for x in elements[self.cardinal // 2: self.cardinal]]
        self.cardinal_gauche = len(self.__lg)
        assert self._invariant()

    def __str__(self):
        resultat = "["
        i = 0
        for elem in reversed(self.__lg):
            resultat += elem.__str__()
            if len(self.__ld) != 0 or i < len(self.__lg) - 1:
                resultat += ", "
            i += 1
        i = 0
        for elem in self.__ld:
            resultat += elem.__str__()
            if i < len(self.__ld) - 1:
                resultat += ", "
            i += 1
        resultat += "]"
        return resultat

    def __len__(self):
        return self.cardinal

    def lire_premier(self):
        """Retourne le premier élément"""
        return self.__lg[-1]

    def inserer_premier(self, x):
        self.__lg.append(x)
        self.cardinal_gauche += 1
        self.cardinal += 1
        assert self._invariant()

    def retirer_premier(self):
        if self.cardinal == 1:
            val = self.__ld.pop()
        else:
            val = self.__lg.pop()
            self.cardinal_gauche -= 1
        self.cardinal -= 1
        self._reequilibrer()
        assert self._invariant()
        return val

    def lire_dernier(self):
        return self.__ld[-1]

    def inserer_dernier(self, x):
        self.__ld.append(x)
        self.cardinal += 1
        assert self._invariant()

    def retirer_dernier(self):
        val = self.__ld.pop()
        self.cardinal -= 1
        self._reequilibrer()
        assert self._invariant()
        return val

    def lire_index(self, n):
        if n > len(self.__lg):
            return self.__ld[n - len(self.__lg)]
        else:
            return self.__lg[len(self.__lg) - n - 1]

    def inserer_index(self, n, x):
        if n > self.cardinal_gauche:
            self.__ld.insert(n - self.cardinal_gauche, x)
        else:
            self.__lg.insert(self.cardinal_gauche - n, x)
            self.cardinal_gauche += 1
        self.cardinal += 1
        assert self._invariant()

    def retirer_index(self, n):
        if n < self.cardinal_gauche:
            val = self.__lg.pop(self.cardinal_gauche - n - 1)
            self.cardinal_gauche -= 1
        else:
            val = self.__ld.pop(n - self.cardinal_gauche)
        self.cardinal -= 1
        self._reequilibrer()
        assert self._invariant()
        return val

    def _invariant(self):
        """
        Vérifier que la somme des longueurs des deux vecteurs donne le cardinal.
        :return: True si l'invariant est respecté.
        """
        if self.cardinal_gauche == len(self.__lg):
            return len(self.__lg) + len(self.__ld) == self.cardinal
        return False

    def _reequilibrer(self):
        """
        Si, après un retrait, un des vecteurs est vide, les éléments sont répartis de nouveau sur les deux vecteurs
        de manière à être approximativement égaux.  Si un seul élément est restant il doit être à droite.
        :return: None
        """
        if self.cardinal == 0:
            return
        mid = self.cardinal // 2
        if self.cardinal_gauche == 0:
            copie_gauche = [x for x in reversed(self.__ld[0: mid])]
            copie_droite = [x for x in self.__ld[mid: len(self.__ld)]]
        elif self.cardinal_gauche == self.cardinal:
            copie_gauche = [x for x in self.__lg[mid + 1: self.cardinal_gauche]]
            copie_droite = [x for x in reversed(self.__lg[0: mid + 1])]
        else:
            return
        self.__lg = copie_gauche
        self.__ld = copie_droite
        self.cardinal_gauche = len(self.__lg)





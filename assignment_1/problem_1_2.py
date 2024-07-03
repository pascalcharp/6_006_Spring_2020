from lib.ListeDoublementChainee import ListeDoublementChainee


def renverser(L, i, k):
    assert i + k - 1 < len(L)

    gauche = i
    droite = i + k - 1
    while droite > gauche:
        tmp = L.retirer_index(droite)
        L.inserer_index(droite - 1, L.retirer_index(gauche))
        L.inserer_index(gauche, tmp)
        gauche += 1
        droite -= 1

def deplacer_un_vers_la_droite(L, i, k):
    assert i + k < len(L) and k < len(L)
    L.inserer_index(i, L.retirer_index(i + k))

def deplacer_un_vers_la_gauche(L, i, k):
    assert i > 0 and k < len(L)
    L.inserer_index(i + k - 1, L.retirer_index(i - 1))

def deplacer(L, i, k, j):
    if j > i:
        offset = j - i - k
        for n in range(offset):
            deplacer_un_vers_la_droite(L, i + n, k)
    elif j < i:
        offset = i - j
        for n in range(offset):
            deplacer_un_vers_la_gauche(L, i - n, k)




if __name__ == "__main__":
    #liste = ListeDoublementChainee([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    #renverser(liste, 2, 5)

    liste = ListeDoublementChainee([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # deplacer_un_vers_la_gauche(liste, 2, 5)
    # deplacer_un_vers_la_droite(liste, 1, 5)
    # deplacer(liste, 1, 4, 3)
    # deplacer(liste, 1, 3, 9)
    deplacer(liste, 6, 3, 0)
    print(liste)

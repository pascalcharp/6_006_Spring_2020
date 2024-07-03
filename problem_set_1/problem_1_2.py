from lib.ListeDoublementChainee import ListeDoublementChainee


def swap_ends(liste):
    tmp = liste.retirer_premier()
    liste.inserer_premier(liste.retirer_dernier())
    liste.inserer_dernier(tmp)


def shift_left(liste, k):
    for _ in range(k):
        liste.inserer_dernier(liste.retirer_premier())


if __name__ == "__main__":
    d = ListeDoublementChainee([1, 2, 3, 4, 5])
    swap_ends(d)
    print(d)
    shift_left(d, 3)
    print(d)

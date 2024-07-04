"""
Résolution de l'exercice 1-4 de la session de problème 1 du cours 6.006 Introduction to algorithms du MIT

calculer_dommage_maison_fb et calculer_dommages_fb: réponse de l'exercice 4a (force brute)
calculer_dommage_special: réponse de l'exercice 4b
calculer_dommages_rec: réponse de l'exercice 4c et 4d
"""


def calculer_dommage_maison_fb(briques, numero):
    """Calcule le dommage pour la maison située au numéro passé en paramètre.
    Args :
        briques (int list) : Nombre de brique pour chaque maison
        numero (int) : Numéro de la maison dont on veut connaître le dommage
    Returns :
        int : Le nombre de maisons détruites si le loup souffle sur la maison numéro numero.
    Precondition :
        numero est un indice valide de briques
    Complexité :
        Linéaire (algo en force brute)
        """
    assert numero in range(len(briques))
    dommage = 1
    for i in range(numero + 1, len(briques)):
        if briques[i] < briques[numero]:
            dommage += 1
    return dommage


def calculer_dommages_fb(briques):
    """
    Calcule le dommage pour chaque maison de la liste briques.
    Args :
        briques (int list) : Nombre de brique pour chaque maison
    Returns :
        int list : Pour chaque maison, le nombre total de maisons détruites si le loup souffle sur cette maison.
    Complexité :
        Quadratique (algo en force brute)
    """
    dommages = [0 for _ in range(len(briques))]
    for i in range(len(briques)):
        dommages[i] = calculer_dommage_maison_fb(briques, i)
    return dommages


def calculer_dommages_special(briques):
    """
    Calcule le dommage de chaque maison en présupposant qu'au maximum UNE SEULE maison n'est pas spéciale.
    Rappel : une maison est spéciale si elle n'a pas de voisin à droite, ou si sa voisine de droite lui est strictement
    supérieure.
    Args :
        briques (int list) : Nombre de brique pour chaque maison d'ouest en est
    Returns :
        int list : le dommage résultant pour chaque maison
    Precondition : Il existe UNE et UNE SEULE maison dans briques qui n'est pas spéciale.
    """
    assert len(briques) > 1
    dommage = [1 for _ in range(len(briques))]
    ordinaire = None
    maison_ordinaire_trouvee = False
    for i in range(len(briques) - 1):
        if briques[i] > briques[i + 1]:
            ordinaire = i
            maison_ordinaire_trouvee = True
    assert maison_ordinaire_trouvee
    i = 0
    dommage_courant = 1
    j = ordinaire + 1
    while i < ordinaire + 1:
        if j == len(briques) or briques[i] <= briques[j]:
            dommage[i] = dommage_courant
            i += 1
        elif j < len(briques):
            dommage_courant += 1
            j += 1
    return dommage


def _mise_a_jour_dommages(adresses, briques, dommages, debut, milieu, fin):
    dommage_additionnel = 0
    i = debut
    j = milieu
    while i < milieu:
        if j == fin or briques[adresses[i]] <= briques[adresses[j]]:
            dommages[adresses[i]] += dommage_additionnel
            i += 1
        elif j < fin:
            dommage_additionnel += 1
            j += 1


def _fusionner(adresses, briques, aux, debut, milieu, fin):
    i = debut
    j = milieu
    k = debut
    while i < milieu and j < fin:
        if briques[adresses[i]] <= briques[adresses[j]]:
            aux[k] = adresses[i]
            i += 1
        else:
            aux[k] = adresses[j]
            j += 1
        k += 1
    for ii in range(i, milieu):
        aux[k] = adresses[ii]
        k += 1
    for jj in range(j, fin):
        aux[k] = adresses[jj]
        k += 1
    for i in range(debut, fin):
        adresses[i] = aux[i]


def aux_calculer_dommages(adresses, briques, dommages, aux, debut, fin):
    if fin - debut < 2:
        return
    mid = (debut + fin) // 2
    aux_calculer_dommages(adresses, briques, dommages, aux, debut, mid)
    aux_calculer_dommages(adresses, briques, dommages, aux, mid, fin)
    _mise_a_jour_dommages(adresses, briques, dommages, debut, mid, fin)
    _fusionner(adresses, briques, aux, debut, mid, fin)


def calculer_dommages_rec(briques):
    """
    Calcule le dommage pour chaque maison.
    Args :
        briques (int list) : Nombre de briques pour chaque maison
    Returns :
        (int list) : dommage pour chaque maison, un nombre entier supérieur ou égal à 1
    Complexité :
        n log(n)
    """
    adresses = [i for i in range(len(briques))]
    dommages = [1 for _ in range(len(briques))]
    aux = [0 for _ in range(len(briques))]

    aux_calculer_dommages(adresses, briques, dommages, aux, 0, len(briques))
    return dommages


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    maisons = [34, 57, 70, 19, 48, 2, 94, 7, 63, 75]
    print(calculer_dommages_fb(maisons))
    print(calculer_dommages_rec(maisons))

    maisons_speciales = [10, 60, 40, 5]
    print(calculer_dommages_rec(maisons_speciales))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

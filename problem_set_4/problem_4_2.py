import math
from lib.radix_sort import radix_sort
from lib.ArbreBinaireAVL import ArbreBinaireAVL

revengers = {
    "a": -2,
    "b": -3,
    "c": -4,
    "d": -5,
    "e": -6,
    "f": -0,
    "g": 1,
    "h": 2,
    "i": 3,
    "j": 4,
    "k": 5,
    "l": 6,
    "m": 7,
    "n": 8,
    "o": 9
}


def trouver_log_max(heros):
    mv = min(heros.values())
    if mv < 0:
        mv = -mv
    else:
        mv = 0
    data = [val + mv for val in revengers.values()]
    data = radix_sort(data, 10)
    data = [val - mv for val in data]
    slice = math.floor(math.log2(len(data)))
    return data[-slice:]


def trouver_log_max_logn(heros):
    slice = math.floor(math.log2(len(heros)))
    arbre = ArbreBinaireAVL()
    for nom in heros:
        if len(arbre) < slice:
            arbre.insert(nom, heros[nom])
        else:
            minkey, minval = arbre.minimum()
            if heros[nom] > minval:
                arbre.delete(minkey)
                arbre.insert(nom, heros[nom])
    resultat = []
    for nom, _ in arbre:
        resultat.append(nom)
    return resultat


if __name__ == "__main__":
    print(trouver_log_max_logn(revengers))

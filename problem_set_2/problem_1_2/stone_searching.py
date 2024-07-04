"""
Solution de l'exercice de Sanos et la pierre du sarcasme...

NB : On utilise ici un objet Oracle défini dans oracle.py pour simuler la condition spécifiée dans l'énoncé de la
question : l'oracle ne peut donner qu'une seule information, soit si la pierre se trouve sur une planète de niveau
strictement plus élevé que la planète courante, point final. Sinon il serait trop tentant d'utiliser une condition
du type if (n == k) return... Donc pour notre algorithme, seul l'oracle connaît la réponse...
"""
import math

from oracle import Oracle


def alt_stone_search_from(start, oracle, opcount):
    """Fonction récursive qui recherche la pierre avec l'aide de la fonction oracle, à partir d'un point de départ.

    Args:
    ----
        start (int) : Point de départ de la recherche (nombre entier positif ou nul)
        oracle (int → bool) : Retourne True si la pierre se trouve sur une planète dont le chiffre est strictement
        plus grand que son paramètre d'appel

    Returns:
    -------
        (int) : Le numéro de la planète sur laquelle se trouve la pierre
    """
    if not oracle(start):
        return start, opcount
    delta = 1
    current = start + delta
    previous = current
    while oracle(current):
        opcount += 1
        previous = current
        current = start + delta
        delta *= 2
    return alt_stone_search_from(previous, oracle, opcount)


def stone_search(oracle):
    """
    Fonction qui localise la pierre à l'aide de la fonction oracle. Essentiellement, emballe la fonction récursive
    alt_stone_search_from...

   Args:
   ----
       oracle (int → bool) : Fonction qui retourne True si la pierre se trouve sur une planète dont le chiffre est
       strictement plus grand que le paramètre d'entrée.

    Returns:
    -------
        (int) : le numéro de la planète sur laquelle se trouve la pierre
    """
    return alt_stone_search_from(0, oracle, 0)


if __name__ == '__main__':

    # Test de stone_search pour i allant de 0 à 999...
    with open("resultat.txt", "w") as f:
        o = Oracle()
        i = 1
        while i < 10000:
            o.reset_oracle(i)
            result, count = stone_search(o.oracle)
            assert(i == result)
            if i != 0:
                li = math.log2(i)
                f.write(f"{i},{count},{0.5 * (li * (li + 2) + 2)}\n")
            i = i + 1



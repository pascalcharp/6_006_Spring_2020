import math
import random

DEF_CAPACITY = 13
DEF_MAX_LOAD = 1.0
DEF_MIN_LOAD = 0.5


def simple_integer_hash(n):
    return n


def is_prime(n):
    random.seed()
    if n < 2:
        return False
    elif n % 2 == 0:
        return False
    else:
        for _ in range(5):
            base = random.randint(2, n - 1)
            witness = pow(base, n - 1, n)
            if witness != 1:
                return False
        return True


def next_prime(n):
    if n % 2 == 0:
        n += 1
    for i in range(n + 2, 2 * n, 2):
        if is_prime(i):
            return i
    raise ValueError("Pas de nombre premier trouvé dans l'intervalle attendu.")

if __name__ == "__main__":
    x = 250
    print(next_prime(x))

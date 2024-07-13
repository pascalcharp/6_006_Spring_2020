from lib.sequence import Sequence
from lib.hash_map import HashMap


class HashSequence(Sequence):
    def __init__(self, hash_function, elements=None):
        self.hash_map = HashMap(hash_function)
        self.cardinal = 0
        if elements is None:
            elements = []
        for e in elements:
            self.inserer_dernier(e)

    def __len__(self):
        return self.cardinal

    def __str__(self):
        result = "["
        for i in range(self.cardinal):
            result += self.hash_map.find(i).__str__()
            if i != self.cardinal - 1:
                result += ", "
        result += "]"
        return result


    def lire_premier(self):
        raise NotImplementedError

    def inserer_premier(self, x):
        for k in range(len(self.hash_map) - 1, -1, -1):
            val = self.hash_map.remove(k)
            self.hash_map.insert(k + 1, val)
        self.hash_map.insert(0, x)
        self.cardinal += 1

    def retirer_premier(self):
        retval = self.hash_map.remove(0)
        for i in range(1, self.cardinal):
            val = self.hash_map.remove(i)
            self.hash_map.insert(i - 1, val)
        self.cardinal -= 1

    def lire_dernier(self):
        return self.hash_map.find(self.cardinal - 1)

    def inserer_dernier(self, x):
        self.hash_map.insert(self.cardinal, x)
        self.cardinal += 1

    def retirer_dernier(self):
        val = self.hash_map.remove(self.cardinal - 1)
        self.cardinal -= 1
        return val

    def lire_index(self, n):
        return self.hash_map.find(n)

    def inserer_index(self, n, x):
        for i in range(self.cardinal - 1, n - 1, -1):
            val = self.hash_map.remove(i)
            self.hash_map.insert(i + 1, val)
        self.hash_map.insert(n, x)
        self.cardinal += 1

    def retirer_index(self, n):
        retval = self.hash_map.remove(n)
        for i in range(n + 1, self.cardinal):
            x = self.hash_map.remove(i)
            self.hash_map.insert(i - 1, x)
        self.cardinal -= 1
        return retval

if __name__ == "__main__":
    mySequence = HashSequence(lambda x: x, [10, 20, 30, 40, 50])
    print(mySequence)
    mySequence.retirer_index(2)
    mySequence.inserer_index(1, 15)
    print(mySequence)
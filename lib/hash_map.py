import lib.hash_map_constants

class HashMap:
    def __init__(self, hash, capacity=None, elements=None):
        self.hash = hash
        self.cardinal = 0
        if capacity is None:
            capacity = lib.hash_map_constants.DEFAULT_CAPACITY
        self.capacity = capacity
        self.table = [[] for _ in range(self.capacity)]
        if elements is None:
            elements = []
        for k, v in elements:
            self.insert(k, v)

    def insert(self, key, value):
        self.table[self.hash(key) % self.capacity].append((key, value))
        self.cardinal += 1


def myHash(k):
    return k * 13 + 1001

if __name__=="__main__":
    myHashMap = HashMap(myHash)
    myHashMap.insert(23, "A")
    myHashMap.insert(56, "B")
    myHashMap.insert(299, "C")
    myHashMap.insert(3, "D")
    pass

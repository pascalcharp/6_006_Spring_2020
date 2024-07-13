import random

from lib.set import Set
from lib.hash_map_utilities import DEF_MAX_LOAD, DEF_CAPACITY, DEF_MIN_LOAD
from lib.hash_map_utilities import next_prime
from lib.hash_map_utilities import simple_integer_hash

class HashMapIterator:
    def __init__(self, hash_map):
        self.hash_map = hash_map
        self.current_table = 0
        self.current_list_position = 0
        self.current_object_count = 0

    def __next__(self):
        if self.current_list_position == len(self.hash_map.table[self.current_table]) - 1:
            self.current_table += 1
            self.current_list_position = 0
        else:
            self.current_list_position += 1
        self.current_object_count += 1
        if self.current_object_count == len(self.hash_map):
            raise StopIteration
        return self.hash_map.table[self.current_table][self.current_list_position]




class HashMap(Set):
    def __init__(self, hash_function, capacity=None, elements=None):
        super(HashMap, self).__init__()
        self.hash = hash_function
        if capacity is None:
            self.capacity = DEF_CAPACITY
        else:
            self.capacity = capacity
        self.cardinal = 0
        self.table = [[] for _ in range(self.capacity)]
        if elements is None:
            elements = []
        for k, v in elements:
            self.insert(k, v)

    def __len__(self):
        return self.cardinal

    def __repr__(self):
        result = f"Cardinal = {self.cardinal}\n"
        result += f"Capacity = {self.capacity}\n"
        result += f"Load = {self._load()}\n"
        result += f"Data:\n"
        for k in range(self.capacity):
            result += f"{k} : {self.table[k]}\n"
        return result

    def __iter__(self):
        return HashMapIterator(self)

    def _rehash(self, new_capacity):
        new_table = [[] for _ in range(new_capacity)]
        for t in self.table:
            for k, v in t:
                new_table[self.hash(k) % new_capacity].append((k, v))
        self.table = new_table
        self.capacity = new_capacity

    def _load(self):
        return self.cardinal / self.capacity

    def _enforce_load_policy_on_insert(self):
        if self._load() > DEF_MAX_LOAD:
            self._rehash(next_prime(2 * self.capacity))

    def _enforce_load_policy_on_delete(self):
        if self._load() < DEF_MIN_LOAD:
            self._rehash(next_prime(self.capacity // 2))

    def _index_of(self, k):
        return self.hash(k) % self.capacity

    def _find_key(self, k):
        for key, value in self.table[self._index_of(k)]:
            if key == k:
                return key, value
        return None

    def find(self, key):
        result = self._find_key(key)
        if result is None:
            raise KeyError(f"find: Clé {key} non trouvée.")
        return result[1]

    def insert(self, key, value):
        if self._find_key(key) is not None:
            raise KeyError(f"insert: Clé {key} déjà présente.")
        else:
            self.table[self._index_of(key)].append((key, value))
            self.cardinal += 1
            self._enforce_load_policy_on_insert()

    def remove(self, key):
        result = self._find_key(key)
        if result is None:
            raise KeyError("remove: Clé {key} non trouvée.")
        retval = result[1]
        self.table[self._index_of(key)].remove(result)
        self.cardinal -= 1
        self._enforce_load_policy_on_delete()
        return retval

    def keys(self):
        result = []
        for liste in self.table:
            for k, _ in liste:
                result.append(k)
        return result


if __name__ == "__main__":
    myTable = HashMap(simple_integer_hash, elements=[(123, 12), (15674, 12), (9543, 12), (2879, 12)])
    print(myTable.__repr__())
    for _ in range(100):
        myTable.insert(random.randint(0, 100000), 123)
        print(myTable.__repr__())

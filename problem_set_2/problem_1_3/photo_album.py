import unittest
from lib.ListeDoublementChaineeAux import ListeDoublementChaineeAux


class ImageNode:
    def __init__(self, id, image=None):
        self.id = id
        self.image = image
        self.next = None
        self.prev = None

    def __lt__(self, other):
        return self.id < other

    def __gt__(self, other):
        return self.id > other

    def __eq__(self, other):
        return self.id == other


class PhotoAlbum:
    def __init__(self):
        self.images = ListeDoublementChaineeAux()
        self.index = []
        self.cardinal = 0
        assert self._invariant()

    def __repr__(self):
        result = f"Cardinal = {self.cardinal}\n"
        result += f"Images = {self.images.__str__()}\n"
        result += f"Index = {self.index}\n"
        return result

    def _invariant(self):
        if len(self.images) != self.cardinal:
            return False
        if len(self.index) != len(self.images):
            return False
        set_images = set(self.images)
        if len(set_images) != len(self.index):
            return False
        setindexes = set()
        for index in self.index:
            setindexes.add(index.id)
        return setindexes == set_images

    def _search_id_in(self, n, lo, hi):
        if lo > hi:
            return hi
        mid = (lo + hi) // 2
        if self.index[mid] > n:
            return self._search_id_in(n, lo, mid - 1)
        elif self.index[mid] < n:
            return self._search_id_in(n, mid + 1, hi)
        elif self.index[mid] == n:
            return mid

    def search_id(self, n):
        if len(self.index) == 0:
            return 0
        if self.index[0] > n:
            return -1
        return self._search_id_in(n, 0, self.cardinal - 1)

    def __len__(self):
        return self.cardinal

    def import_image(self, id, image):
        node_ref = self.images.aux_insert_last(id, image)
        idx = self.search_id(id)
        if idx < len(self.index) and self.index[idx] == id:
            raise KeyError(f"Identificateur {id} déjà présent dans l'album")
        self.index.insert(idx + 1, node_ref)
        self.cardinal += 1

    def display(self):
        print(self.images.keys())

    def move_below(self, id_a, id_b):
        node_x = self.index[self.search_id(id_a)]
        node_y = self.index[self.search_id(id_b)]
        self.images.aux_insert_node(node_y, self.images.aux_remove_node(node_x))


if __name__ == "__main__":
    a = PhotoAlbum()
    a.import_image(42, None)
    a.import_image(12, None)
    a.import_image(99, None)
    a.import_image(25, None)
    a.import_image(1, None)
    a.display()
    a.move_below(25, 12)
    a.display()

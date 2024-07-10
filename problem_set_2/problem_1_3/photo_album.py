import unittest


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
        self.images = []
        self.index = []
        self.cardinal = 0
        assert self._invariant()

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
        if self.index[0] > n:
            return -1
        return self._search_id_in(n, 0, self.cardinal - 1)

    def __len__(self):
        return self.cardinal

    def import_image(self, id, image):
        new_node = ImageNode(id, image)



if __name__ == "__main__":
    a = PhotoAlbum()

class BiSequence:
    def __init__(self, elements=None):
        self.right = []
        self.left = []
        if elements is None:
            elements = []
        else:
            self._distribute_elements(elements)
        self.offset = len(self.left)

    def _distribute_elements(self, elements):
        mid = len(elements) // 2
        for i in range(mid, len(elements)):
            self.right.append(elements[i])
        for j in range(mid - 1, -1, -1):
            self.left.append(elements[j])

    def __len__(self):
        return len(self.left) + len(self.right)

    def __getitem__(self, i):
        if i - self.offset < 0:
            return self.left[self.offset - i - 1]
        else:
            return self.right[i - self.offset]

    def __setitem__(self, i, value):
        if i - self.offset < 0:
            self.left[self.offset - i - 1] = value
        else:
            self.right[i - self.offset] = value

    def __iter__(self):
        return iter(self.left)

    def __str__(self):
        resultat = "["
        for i in range(len(self.left) - 1, -1, -1):
            resultat += self.left[i].__str__()
            if i != 0:
                resultat += ", "
        if len(self.right) != 0:
            resultat += ", "
        for j in range(len(self.right)):
            resultat += self.right[j].__str__()
            if j != len(self.right) - 1:
                resultat += ", "
        resultat += "]"
        return resultat

    def __repr__(self):
        resultat = f"Left : {self.offset} Right: {len(self.right)} Total: {len(self)}\n"
        resultat += "Left: ["
        for i in range(len(self.left)):
            resultat += self.left[i].__str__()
            if i != len(self.left) - 1:
                resultat += ", "
        resultat += "]\n"
        resultat += "Right: ["
        for i in range(len(self.right)):
            resultat += self.right[i].__str__()
            if i != len(self.right) - 1:
                resultat += ", "
        resultat += "]\n"
        resultat += self.__str__()
        return resultat

    def append(self, element):
        self.right.append(element)

    def prepend(self, element):
        self.left.append(element)
        self.offset += 1

    def insert(self, i, element):
        if i >= self.offset:
            self.right.insert(i - self.offset, element)
        else:
            self.left.insert(self.offset - i - 1, element)
            self.offset += 1

    def pop(self, i):
        if i >= self.offset:
            val = self.right[i - self.offset]
            self.right.pop(i - self.offset)
        else:
            val = self.left[self.offset - i - 1]
            self.left.pop(self.offset - i - 1)
            self.offset -= 1
        self.rebalance()
        return val

    def pop_last(self):
        return self.pop(len(self) - 1)

    def pop_first(self):
        return self.pop(0)

    def rebalance(self):
        if self.offset == len(self.right):
            return
        if self.offset == 0:
            elements = self.right
            self.right = []
        elif len(self.right) == 0:
            elements = self.left
            self.left = []
        else:
            return
        self._distribute_elements(elements)
        self.offset = len(self.left)


if __name__ == "__main__":
    seq = BiSequence([1, 2, 3, 4, 5, 6, 7])
    for i in range(len(seq)):
        print(seq.pop_last())
        print(seq.__repr__())
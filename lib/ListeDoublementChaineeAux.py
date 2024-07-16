class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"Node(key={self.key}, value={self.value}, prev={self.prev}, next={self.next})"

    def __str__(self):
        return f"Node(key={self.key}, value={self.value})"

    def __lt__(self, other):
        return self.key < other

    def __gt__(self, other):
        return self.key > other

    def __eq__(self, other):
        return self.key == other


class ListeDoublementChaineeAuxIterateur:
    def __init__(self, premier, dernier):
        self._courant = premier
        self._dernier = dernier

    def __next__(self):
        self._courant = self._courant.next
        if self._courant == self._dernier:
            raise StopIteration
        return self._courant


class ListeDoublementChaineeAux:
    def __init__(self):
        self.first = Node(None, None)
        self.last = Node(None, None)
        self.first.next = self.last
        self.last.prev = self.first
        self.cardinal = 0
        assert self.invariant()

    def __iter__(self):
        return ListeDoublementChaineeAuxIterateur(self.first, self.last)

    def __len__(self):
        return self.cardinal

    def invariant(self):
        p = self.first.next
        for _ in range(self.cardinal):
            p = p.next
        if p != self.last:
            return False
        p = p.prev
        for _ in range(self.cardinal):
            p = p.prev
        return p == self.first

    def aux_insert_last(self, key, value):
        new_node = Node(key, value)
        new_node.prev = self.last.prev
        self.last.prev.next = new_node
        self.last.prev = new_node
        new_node.next = self.last
        self.cardinal += 1
        assert self.invariant()
        return new_node

    def aux_insert_first(self, key, value):
        new_node = Node(key, value)
        new_node.prev = self.first
        new_node.next = self.first.next
        self.first.next.prev = new_node
        self.first.next = new_node
        self.cardinal += 1
        assert self.invariant()
        return new_node

    def aux_insert_node(self, node, new_node):
        node.prev.next = new_node
        new_node.prev = node.prev
        node.prev = new_node
        new_node.next = node
        self.cardinal += 1
        assert self.invariant()

    def aux_remove_node(self, node):
        rem_node = node
        node.prev.next = node.next
        node.next.prev = node.prev
        self.cardinal -= 1
        assert self.invariant()
        return node

    def keys(self):
        result = []
        for n in self:
            result.append(n.key)
        return result


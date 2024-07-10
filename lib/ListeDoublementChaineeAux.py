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


class ListeDoublementChaineeAux:
    def __init__(self):
        self.first = Node(None, None)
        self.last = Node(None, None)
        self.first.next = self.last
        self.last.prev = self.first
        self.cardinal = 0
        assert self.invariant()

    def __len__(self):
        return self.cardinal

    def invariant(self):
        if self.cardinal == 0:
            return self.first is None and self.last is None
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

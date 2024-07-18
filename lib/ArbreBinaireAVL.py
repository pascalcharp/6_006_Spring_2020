class _Node:
    def __init__(self, key, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0


class ArbreBinaireAVLIterateur:
    def __init__(self, arbre):
        self.current = None
        self.arbre = arbre
        self.minimum = arbre.subtree_minimum(arbre.root)
        self.maximum = arbre.subtree_maximum(arbre.root)

    def __next__(self):
        if self.current == self.maximum:
            raise StopIteration
        if self.current is None:
            self.current = self.minimum
        elif self.current.right is None:
            while self.current == self.current.parent.right:
                self.current = self.current.parent
            self.current = self.current.parent
        else:
            self.current = self.arbre.subtree_minimum(self.current.right)
        return self.current.key, self.current.val


class ArbreBinaireAVL:
    def __init__(self, pairs=None):
        self.root = None
        self.cardinal = 0
        if pairs is None:
            pairs = []
        self.pairs = pairs
        for k, v in pairs:
            self.insert(k, v)
        assert self._invariant()

    def __iter__(self):
        return ArbreBinaireAVLIterateur(self)

    def __len__(self):
        return self.cardinal

    def insert(self, key, val=None):
        self.root = self.subtree_insert(self.root, key, val)
        self.root.parent = None
        self.cardinal += 1
        assert self._invariant()

    def delete(self, key):
        self.root = self.subtree_delete(self.root, key)
        self.cardinal -= 1
        assert self._invariant()

    def lire(self, key):
        return self.subtree_read(self.root, key)

    def minimum(self):
        node = self.subtree_minimum(self.root)
        return node.key, node.val

    def maximum(self):
        node = self.subtree_maximum(self.root)
        return node.key, node.val

    def subtree_height(self, root):
        if root is None:
            return -1
        return root.height

    def subtree_factor(self, root):
        if root is None:
            return 0
        return self.subtree_height(root.right) - self.subtree_height(root.left)

    def subtree_is_skewed_right(self, root):
        return self.subtree_height(root.right) > self.subtree_height(root.left)

    def subtree_is_skewed_left(self, root):
        return self.subtree_height(root.left) > self.subtree_height(root.right)

    def subtree_update_height(self, root):
        if root is None:
            return
        root.height = 1 + max(self.subtree_height(root.left), self.subtree_height(root.right))

    def subtree_minimum(self, root):
        while root.left is not None:
            root = root.left
        return root

    def subtree_maximum(self, root):
        while root.right is not None:
            root = root.right
        return root

    def subtree_rotate_right(self, root):
        new_root = root.left
        root.left = new_root.right
        if new_root.right is not None:
            new_root.right.parent = root
        new_root.right = root
        root.parent = new_root
        root = new_root
        self.subtree_update_height(root.right)
        return root

    def subtree_rotate_left(self, root):
        new_root = root.right
        root.right = new_root.left
        if new_root.left is not None:
            new_root.left.parent = root
        new_root.left = root
        root.parent = new_root
        root = new_root
        self.subtree_update_height(root.left)
        return root

    def subtree_balance(self, root):
        factor = self.subtree_factor(root)
        if factor < -1:
            if self.subtree_is_skewed_right(root.left):
                root.left = self.subtree_rotate_left(root.left)
                root.left.parent = root
            root = self.subtree_rotate_right(root)
        elif factor > 1:
            if self.subtree_is_skewed_left(root.right):
                root.right = self.subtree_rotate_right(root.right)
                root.right.parent = root
            root = self.subtree_rotate_left(root)
        self.subtree_update_height(root)
        return root

    def subtree_insert(self, root, key, val):
        if root is None:
            root = _Node(key, val)
        elif key < root.key:
            root.left = self.subtree_insert(root.left, key, val)
            root.left.parent = root
        elif key > root.key:
            root.right = self.subtree_insert(root.right, key, val)
            root.right.parent = root
        else:
            raise KeyError("insertion: Duplicata de clé")
        root = self.subtree_balance(root)
        return root

    def subtree_delete(self, root, key):
        if root is None:
            raise KeyError("retrait: clé absente")
        if key < root.key:
            root.left = self.subtree_delete(root.left, key)
            if root.left is not None:
                root.left.parent = root
        elif key > root.key:
            root.right = self.subtree_delete(root.right, key)
            if root.right is not None:
                root.right.parent = root
        else:
            if root.left is None:
                if root.right is None:
                    root = None
                else:
                    target = self.subtree_minimum(root.right)
                    root.key = target.key
                    root.val = target.val
                    root.right = self.subtree_delete(root.right, target.key)
                    if root.right is not None:
                        root.right.parent = root
            else:
                target = self.subtree_maximum(root.left)
                root.key = target.key
                root.val = target.val
                root.left = self.subtree_delete(root.left, target.key)
                if root.left is not None:
                    root.left.parent = root
        root = self.subtree_balance(root)
        return root

    def subtree_read(self, root, key):
        if root is None:
            raise KeyError("lire: clé absente")
        if key < root.key:
            return self.subtree_read(root.left, key)
        elif key > root.key:
            return self.subtree_read(root.right, key)
        else:
            return root.val

    def _invariant(self):
        if self.cardinal == 0:
            return self.root is None
        key_list = []
        for key, _ in self:
            key_list.append(key)
        first = key_list[0]
        for i in range(1, len(key_list)):
            second = key_list[i]
            if second <= first:
                return False
            first = second
        return True


if __name__ == '__main__':
    myKeys = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
    myTuples = [(k, None) for k in myKeys]
    monArbre = ArbreBinaireAVL(myTuples)
    for k, v in monArbre:
        print(k, v)

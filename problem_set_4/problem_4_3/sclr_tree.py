from lib.ArbreBinaireAVL import ArbreBinaireAVL


class AuctionBidKey:
    def __init__(self, id_number, bid):
        self.bid = bid
        self.id_number = id_number

    def __lt__(self, other):
        if self.bid == other.bid:
            return self.id_number < other.id_number
        return self.bid < other.bid

    def __gt__(self, other):
        return other < self

    def __eq__(self, other):
        return self.bid == other.bid and self.id_number == other.id_number

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        return not self.__gt__(other)


class AuctionTree(ArbreBinaireAVL):
    def __init__(self, k_max, bidders=None):
        super().__init__()
        self.k_number = k_max
        if bidders is None:
            bidders = []
        for id, bid in bidders:
            self.insert(id, bid)

    def insert(self, id, bid=None):
        bid_key = AuctionBidKey(id, bid)
        bid_value = bid
        if self.cardinal < self.k_number:
            self.root = self.subtree_insert(self.root, bid_key, bid_value)
            self.cardinal += 1
        else:
            min_key, min_node = self.minimum()
            if bid_key.bid > min_key.bid:
                self.delete(min_key)
                self.insert(id, bid)

    def sum(self):
        return self.root.val

    def subtree_sum(self, root):
        if root is None:
            return 0
        return root.val

    def subtree_update_sum(self, root):
        if root is not None:
            root.val = root.key.bid + self.subtree_sum(root.left) + self.subtree_sum(root.right)
        return root

    def subtree_insert(self, root, key, node_info):
        root = super().subtree_insert(root, key, node_info)
        root = self.subtree_update_sum(root)
        return root

    def subtree_balance(self, root):
        root = super().subtree_balance(root)
        root = self.subtree_update_sum(root)
        return root

    def subtree_rotate_left(self, root):
        root = super().subtree_rotate_left(root)
        root.left = self.subtree_update_sum(root.left)
        root = self.subtree_update_sum(root)
        return root

    def subtree_rotate_right(self, root):
        root = self.subtree_rotate_right(root)
        root.right = self.subtree_update_sum(root.right)
        root = self.subtree_update_sum(root)
        return root


if __name__ == '__main__':
    bidders = [
        ("A", 100),
        ("B", 200),
        ("C", 300),
        ("D", 400),
        ("E", 500),
        ("F", 600),
        ("G", 700),
        ("H", 800),
        ("I", 900),
        ("J", 1000),
    ]
    tree = AuctionTree(4, bidders)
    print(tree.sum())

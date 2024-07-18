from lib.ArbreBinaireAVL import ArbreBinaireAVL, _Node


class AuctionTreeNode:
    def __init__(self, bid):
        self.bid = bid
        self.sum = bid


class AuctionTree(ArbreBinaireAVL):
    def __init__(self, k_max, bidders=None):
        super().__init__()
        self.k_number = k_max
        if bidders is None:
            bidders = []
        for k, b in bidders:
            self.insert(k, b)

    def insert(self, key, val=0):
        if self.cardinal < self.k_number:
            self.root = self.subtree_insert(self.root, key, AuctionTreeNode(val))
            self.cardinal += 1
        else:
            min_key, min_node = self.minimum()
            if val > min_node.bid:
                self.delete(min_key)
                self.insert(key, val)

    def sum(self):
        return self.root.val.sum

    def subtree_sum(self, root):
        if root is None:
            return 0
        return root.val.sum

    def subtree_update_sum(self, root):
        if root is not None:
            root.val.sum = root.val.bid + self.subtree_sum(root.left) + self.subtree_sum(root.right)
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

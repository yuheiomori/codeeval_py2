# coding=utf-8
import sys


class Tree(object):
    def __init__(self, x):
        self.left = None
        self.value = x
        self.right = None

    def insert(self, x):
        if x == self.value:
            return self
        elif x < self.value:

            if self.left:
                self.left.insert(x)
            else:
                self.left = Tree(x)
        else:
            if self.right:
                self.right.insert(x)
            else:
                self.right = Tree(x)
        return self

    @classmethod
    def create_from_list(cls, l):
        tree = Tree(l[0])
        for x in l[1:]:
            tree.insert(x)
        return tree


def find_lca(tree, p, q):
    if tree is None:
        return None
    if (tree.left is not None and tree.left.value == p) or\
            (tree.left is not None and tree.left.value == q) or\
            (tree.right is not None and tree.right.value == p) or\
            (tree.right is not None and tree.right.value == q):
        return tree
    else:
        l = find_lca(tree.left, p, q)
        r = find_lca(tree.right, p, q)

        if l is not None and r is not None:
            return tree
        elif l is not None:
            return l
        else:
            return r

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for line in test_cases:
        t = Tree.create_from_list([30, 8, 52, 3, 20, 10, 29])
        p1, p2 = [int(e) for e in line.rstrip().split(' ')]
        print(find_lca(t, p1, p2).value)

    test_cases.close()

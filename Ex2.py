class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = node
                    break
                current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = node
                    break
                current = current.right
            else:
                break

    def _find_min(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node

    def remove(self, data):
        self.root = self._remove(self.root, data)

    def _remove(self, node, data):
        if node is None:
            return None

        if data < node.data:
            node.left = self._remove(node.left, data)
        elif data > node.data:
            node.right = self._remove(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._find_min(node.right)
                node.data = temp.data
                node.right = self._remove(node.right, temp.data)
        return node

    def max_height(self):
        return self._max_height(self.root)

    def _max_height(self, node):
        if node is None:
            return 0
        return 1 + max(self._max_height(node.left), self._max_height(node.right))

    def n_parents(self):
        return self._n_parents(self.root)

    def _n_parents(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 0
        return 1 + self._n_parents(node.left) + self._n_parents(node.right)

    def n_children(self):
        return self._n_children(self.root) - 1

    def _n_children(self, node):
        if node is None:
            return 0
        return 1 + self._n_children(node.left) + self._n_children(node.right)

    def n_leaves(self):
        return self._n_leaves(self.root)

    def _n_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._n_leaves(node.left) + self._n_leaves(node.right)

    def n_sibling(self):
        return self._n_sibling(self.root)

    def _n_sibling(self, node):
        if node is None:
            return 0
        if node.left is not None and node.right is not None:
            return 1 + self._n_sibling(node.left) + self._n_sibling(node.right)
        return self._n_sibling(node.left) + self._n_sibling(node.right)

    def print_depth(self):
        self._print_depth(self.root, 0)

    def _print_depth(self, node, depth):
        if node is None:
            return
        print('-' * depth, node.data)
        self._print_depth(node.left, depth + 1)
        self._print_depth(node.right, depth + 1)


def main():
    bst = BinarySearchTree()
    data = [50, 25, 75, 30, 60, 40, 35, 70, 90, 15, 45, 27, 55, 85, 100]
    for d in data:
        bst.insert(d)

    bst.print_depth()

    bst.remove(30)
    bst.remove(75)
    bst.remove(35)

    print("After removing 30, 75, 35")
    bst.print_depth()

    print('Max Height:', bst.max_height())
    print('Parents:', bst.n_parents())
    print('Children:', bst.n_children())
    print('Leaves:', bst.n_leaves())
    print('Siblings:', bst.n_sibling())


if __name__ == '__main__':
    main()
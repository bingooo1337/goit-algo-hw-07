from binary_tree import BinarySearchTree


def find_min_tree_value(tree: BinarySearchTree):
    current = tree.root
    while current.left is not None:
        current = current.left
    return current.key

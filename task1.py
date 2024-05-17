from binary_tree import BinarySearchTree


def find_max_tree_value(tree: BinarySearchTree):
    current = tree.root
    while current.right is not None:
        current = current.right
    return current.key

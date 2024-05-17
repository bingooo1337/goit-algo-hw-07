from binary_tree import BinarySearchTree, TreeNode


def tree_sum(tree: BinarySearchTree):
    return _subtree_sum(tree.root)


def _subtree_sum(node: TreeNode):
    if node is None:
        return 0
    else:
        return node.key + _subtree_sum(node.left) + _subtree_sum(node.right)

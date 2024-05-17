from binary_tree import BinarySearchTree
from task1 import find_max_tree_value
from task2 import find_min_tree_value
from task3 import tree_sum


tree = BinarySearchTree()
tree.insert(10)
tree.insert(20)
tree.insert(5)
tree.insert(25)
tree.insert(15)
tree.insert(35)
tree.insert(65)
tree.insert(30)
tree.insert(0)


print("Max value:", find_max_tree_value(tree))
print("Min value:", find_min_tree_value(tree))
print("Sum value:", tree_sum(tree))

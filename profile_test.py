from bst import BST
import random

tree = BST()
l = list(range(10000000))
random.shuffle(l)
for i in l:
    tree.insert(i)

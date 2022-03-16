from bst import BST
import random

import logging
logging.disable(logging.INFO)


tree = BST()
numbers = list(range(1000000))
random.shuffle(numbers)
for i in numbers:
    tree.insert(i)

random.shuffle(numbers)
for i in numbers:
    tree = tree.delete(i)

if __name__ == '__main__':
    pass

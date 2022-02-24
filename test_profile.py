from bst import BST
import random

import logging
# import cProfile
# import ptest

logging.disable(logging.INFO)


tree = BST()
l = list(range(1000000))
random.shuffle(l)
for i in l:
    tree.insert(i)

if __name__ == '__main__':
    pass
    # cProfile.run('.main()')
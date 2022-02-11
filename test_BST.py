import unittest
from bst import BST    # bst - название основного файла, BST - функция


class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def many_insert(self, a):
        for num in a:
            self.bst.insert(num[0], num[1])


class Test_Delete(TestBST):
    def test_delete_without_elements(self):
        self.bst = self.bst.delete(11)
        self.assertEqual(self.bst.key, None)
        self.assertEqual(self.bst.data, None)
        self.assertEqual(self.bst.left, None)
        self.assertEqual(self.bst.right, None)

    def test_delete_not_existing_elem(self):
        self.bst.insert(10, 'что-то 10')
        self.bst = self.bst.delete(11)
        self.assertEqual(self.bst.key, 10)
        self.assertEqual(self.bst.left, None)
        self.assertEqual(self.bst.right, None)
        self.assertEqual(self.bst.data, 'что-то 10')

    def test_delete_root_without_kids(self):
        self.bst.insert(11, 'что-то 11')
        self.bst = self.bst.delete(11)
        self.assertEqual(self.bst.key, None)
        self.assertEqual(self.bst.data, None)

    def test_delete_root_with_left(self):
        self.many_insert([[11, 'что-то 11'], [9, 'что-то 9']])
        self.bst = self.bst.delete(11)
        self.assertEqual(self.bst.key, 9)
        self.assertEqual(self.bst.left, None)
        self.assertEqual(self.bst.data, 'что-то 9')

    def test_delete_root_with_right(self):
        self.many_insert([[8, 'что-то 8'], [9, 'что-то 9']])
        self.bst = self.bst.delete(8)
        self.assertEqual(self.bst.key, 9)
        self.assertEqual(self.bst.right, None)
        self.assertEqual(self.bst.data, 'что-то 9')

    def test_delete_root_with_kids(self):
        self.many_insert([[11, 'что-то 11'], [9, 'что-то 9'], [15, 'что-то 15'], [13, 'что-то 13']])
        self.bst = self.bst.delete(11)
        self.assertEqual(self.bst.key, 13)
        self.assertEqual(self.bst.right.key, 15)
        self.assertEqual(self.bst.left.key, 9)
        self.assertEqual(self.bst.right.right, None)
        self.assertEqual(self.bst.data, 'что-то 13')

    def test_delete_left_without_kids(self):
        self.many_insert([[11, 'что-то 11'], [9, 'что-то 9']])
        self.bst = self.bst.delete(9)
        self.assertEqual(self.bst.left, None)

    def test_delete_left_with_left(self):
        self.many_insert([[11, 'что-то 11'], [9, 'что-то 9'], [7, 'что-то 7']])
        self.bst = self.bst.delete(9)
        self.assertEqual(self.bst.left.key, 7)
        self.assertEqual(self.bst.left.left, None)
        self.assertEqual(self.bst.left.data, 'что-то 7')

    def test_delete_left_with_right(self):
        self.many_insert([[11, 'что-то 11'], [9, 'что-то 9'], [10, 'что-то 10']])
        self.bst = self.bst.delete(9)
        self.assertEqual(self.bst.left.key, 10)
        self.assertEqual(self.bst.left.right, None)
        self.assertEqual(self.bst.left.data, 'что-то 10')

    def test_delete_left_with_kids(self):
        self.many_insert([[11, 'что-то 11'], [9, 'что-то 9'], [10, 'что-то 10'], [7, 'что-то 7']])
        self.bst = self.bst.delete(9)
        self.assertEqual(self.bst.left.key, 10)
        self.assertEqual(self.bst.left.right, None)
        self.assertEqual(self.bst.left.data, 'что-то 10')


    def test_delete_right_without_kids(self):
        self.many_insert([[11, 'что-то 11'], [15, 'что-то 15']])
        self.bst = self.bst.delete(15)
        self.assertEqual(self.bst.right, None)

    def test_delete_right_with_left(self):
        self.many_insert([[11, 'что-то 11'], [15, 'что-то 15'], [13, 'что-то 13']])
        self.bst = self.bst.delete(15)
        self.assertEqual(self.bst.right.key, 13)
        self.assertEqual(self.bst.right.left, None)
        self.assertEqual(self.bst.right.data, 'что-то 13')

    def test_delete_right_with_right(self):
        self.many_insert([[11, 'что-то 11'], [15, 'что-то 15'], [17, 'что-то 17']])
        self.bst = self.bst.delete(15)
        self.assertEqual(self.bst.right.key, 17)
        self.assertEqual(self.bst.right.right, None)
        self.assertEqual(self.bst.right.data, 'что-то 17')

    def test_delete_right_with_kids(self):
        self.many_insert([[11, 'что-то 11'], [15, 'что-то 15'], [16, 'что-то 16'], [13, 'что-то 13']])
        self.bst = self.bst.delete(15)
        self.assertEqual(self.bst.right.key, 16)
        self.assertEqual(self.bst.right.right, None)
        self.assertEqual(self.bst.right.left.key, 13)
        self.assertEqual(self.bst.right.data, 'что-то 16')
        self.assertEqual(self.bst.right.left.data, 'что-то 13')


class Test_Insert(TestBST): # вставка не чисел, не целых
    def test_insert_no_num_key(self):
        self.bst.insert('asdasd', 123)
        self.assertEqual(self.bst.key, None)
        self.assertEqual(self.bst.data, None)

    def test_insert_float_key(self):
        self.bst.insert(123.54, 123.32)
        self.assertEqual(self.bst.key, None)
        self.assertEqual(self.bst.data, None)

    def test_create_object_with_key(self):
        link = BST(10, 10)
        self.assertEqual(link.key, 10)
        self.assertEqual(link.data, 10)

    def test_insert_root(self):
        self.bst.insert(1, 'что-то 1')
        self.assertEqual(self.bst.key, 1)
        self.assertEqual(self.bst.data, 'что-то 1')

    def test_insert_right(self):
        self.many_insert([[1, 'что-то 1'], [5, 'что-то 5']])
        self.assertEqual(self.bst.right.key, 5)
        self.assertEqual(self.bst.right.data, 'что-то 5')

    def test_insert_left(self):
        self.many_insert([[4, 'что-то 4'], [-1, 'что-то -1']])
        self.assertEqual(self.bst.left.key, -1)
        self.assertEqual(self.bst.left.data, 'что-то -1')

    def test_insert_left_left(self):
        self.many_insert([[5, 'что-то 5'], [3, 'что-то 3'], [-1, 'что-то -1']])
        self.assertEqual(self.bst.left.left.key, -1)
        self.assertEqual(self.bst.left.left.data, 'что-то -1')

    def test_insert_left_right(self):
        self.many_insert([[5, 'что-то 5'], [3, 'что-то 3'], [4, 'что-то 4']])
        self.assertEqual(self.bst.left.right.key, 4)
        self.assertEqual(self.bst.left.right.data, 'что-то 4')

    def test_insert_right_left(self):
        self.many_insert([[5, 'что-то 5'], [7, 'что-то 7'], [6, 'что-то 6']])
        self.assertEqual(self.bst.right.left.key, 6)
        self.assertEqual(self.bst.right.left.data, 'что-то 6')

    def test_insert_right_right(self):
        self.many_insert([[5, 'что-то 5'], [7, 'что-то 7'], [9, 'что-то 9']])
        self.assertEqual(self.bst.right.right.key, 9)
        self.assertEqual(self.bst.right.right.data, 'что-то 9')

    def test_insert_duplicate(self):
        self.many_insert([[5, 'что-то 5'], [5, 'что-то 5'], [5, 'что-то 5']])
        self.assertEqual(self.bst.key, 5)
        self.assertEqual(self.bst.data, 'что-то 5')
        self.assertEqual(self.bst.right, None)
        self.assertEqual(self.bst.left, None)


class Test_Search(TestBST):
    def setUp(self):
        self.bst = BST()
        self.many_insert([[50, '5'], [26, '5'], [62, '62'], [17, '17'], [45, '45'], [3, '3'], [31, '31'], [48, '48']])

    def test_search_root(self):
        el = self.bst.search_element(50)
        self.assertEqual(el.key, 50)

    def test_search_left(self):
        el = self.bst.search_element(26)
        self.assertEqual(el.key, 26)

    def test_search_right(self):
        el = self.bst.search_element(62)
        self.assertEqual(el.key, 62)

    def test_search_left_left(self):
        el = self.bst.search_element(17)
        self.assertEqual(el.key, 17)

    def test_search_left_right(self):
        el = self.bst.search_element(45)
        self.assertEqual(el.key, 45)

    def test_search_not_existing_element(self):
        el = self.bst.search_element(55)
        self.assertEqual(el, None)

    def test_double_search(self):
        el = self.bst.search_element(62)
        self.assertEqual(el.key, 62)
        el = self.bst.search_element(62)
        self.assertEqual(el.key, 62)


class Test_bypass(TestBST):
    def test_bypass(self):
        self.many_insert([[50, '50'], [26, '26'], [62, '62'], [17, '17'], [45, '45'], [3, '3'], [31, '31'], [48, '48']])
        path = self.bst.bypass(0, [0])
        self.assertEqual(path, [3, [50, '50'], [26, '26'], [17, '17'], [3, '3'], [17, None], [26, None], [45, '45'],
                                [31, '31'], [45, None], [48, '48'], [45, None], [26, None], [50, None], [62, '62'],
                                [50, None]])

    def test_bypass_without_element(self):
        path = self.bst.bypass(0, [0])
        self.assertEqual(path, [0])

    def test_bypass_with_one_element(self):
        self.many_insert([[50, '50']])
        path = self.bst.bypass(0, [0])
        self.assertEqual(path, [0, [50, '50']])


if __name__ == '__main__':
    pass

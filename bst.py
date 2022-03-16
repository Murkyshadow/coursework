import logging

logging.basicConfig(level=logging.INFO)
# logging.disable(logging.INFO)


class Tree:
    """
    Структура данных словарь на основе двоичного дерева поиска
    """
    def __init__(self, key=None, data=None):
        self.left = None
        self.right = None
        self.key = key
        self.data = data


class BST(Tree):
    """
    В этом классе находятся все функции для взаимодействия с деревом (удаление, добавление, поиск)
    """
    def insert(self, key, data=None):
        """
        Осуществляется вставка элемента в дерево.
        :param key: ключ, по которому осуществляется доступ к данным в дереве (его мы вставляем в дерево).
        :param data: данные, которые вставляем вместе с ключем.
        :return: None
        """
        try:
            int(key)        # в spiner вводятся числа строкой (string)
        except ValueError:
            return self

        if int(key) != float(key):
            return self

        key = int(key)

        if self.key is None:  # если в нем нет данных (такое может возникнуть при удалении всех элементов)
            self.key = key
            self.data = data
            logging.log(logging.INFO, f' вы вставили: {key}, {data}')

        else:
            if key < self.key:  # если меньше значит идем в левое поддерево
                if self.left is None:  # если левое поддерево пустое, тогда создаем новый объект (новое поддерево), передаем само значение и записываем ссылку на него в left
                    self.left = BST(key, data)
                    logging.log(logging.INFO, f' вы вставили: {key}, {data}')

                else:  # если не пустое, тогда спускаемся в левое поддерево и пытаемся снова записать значение в дерево
                    self.left.insert(key, data)

            elif key > self.key:  # если больше идем в правое поддерево
                if self.right is None:  # если правое поддерево пустое, тогда создаем новый объект (новое поддерево),
                    # передаем само значение и записываем ссылку на него в right
                    self.right = BST(key, data)
                    logging.log(logging.INFO, f' вы вставили: {key}, {data}')

                else:  # если не пустое, тогда спускаемся в поддерево и пытаемся снова записать значение в дерево
                    self.right.insert(key, data)
            else:
                logging.log(logging.INFO, "Такой элемент уже существует!")

    def delete(self, key, root=None):  # удалить элемент: 1) найти элемент, который нужно удалить 2) проверить сколько поддеревьев на удаляемом элементе 3) исходя из кол-ва поддеревьев выбираем способ удаления и удаляем
        """
        функция для удаления элемента в дереве
        :param key: ключ того элемента, который нужно удалить
        :param root: ссылка на самый первый элемент в дереве (корень), она нужна, если удаляется корень без поддеревьев
        :return: возвращаем ссылку на новый элемент, если прошлый элемент удалили
        """
        key = int(key)      # в spiner вводятся числа строкой (string)
        if root is None:
            root = self

        if self.key is None:
            logging.log(logging.INFO, 'кажется элемент, который вы пытаетесь удалить, не существует')
            return self

        if self.key != key:  # не нашли --> поднимаемся дальше по дереву
            if key < self.key and self.left is not None:
                self.left = self.left.delete(key, root)
            elif key > self.key and self.right is not None:
                self.right = self.right.delete(key, root)
            else:
                logging.log(logging.INFO, 'кажется элемент, который вы пытаетесь удалить, не существует')
                return self

        else:  # нашли --> определим сколько поддеревьев
            logging.log(logging.INFO, f'вы удалили: {key}, {self.data}')

            if self.right is None:  # если нет правого --> возможно есть левый или ни одного -->
                temp = self.left  # --> запоминаем ссылку на левый (ну или записываем None в случае, если левого нет)-->

                if root.key == key and self.left is None:  # если удаляем корень без поддеревьев
                    self.key = None
                    self.data = None
                    return self

                del self        # self = None
                return temp     # --> передаем ссылку на новый элемент (или None)

            if self.left is None:  # если нет левого --> значит есть только правый -->
                temp = self.right  # --> запоминаем ссылку на правый -->
                del self  # --> стираем данные (2ой способ) -->
                return temp  # --> передаем ссылку на новый элемент

            # далее останутся, те случаи, где есть оба поддерева --> нам надо найти элемент, который ближе всего к данному элемнту, чтобы поставить его вместо текущего. Таких элемента 2: который немного меньше данного - самый правый в левом поддереве (наибольший) и, который немного больше данного - самый левый в правом поддереве (наименьший) я буду заменять данный элемент на тот, который немного больше -->
            link = self.right.search_min()  # --> найдем элемент, который стоит правее (если выстроить все числа по порядку) - самый левый в правом поддереве (наименьший) -->
            temp = link.key  # --> запомним найденный элемент -->
            temp2 = link.data
            self.delete(link.key, root)  # --> и удаляем элемент (с помощью нашей же функции), который нашли тк мы его записали в тот, который надо удалить
            self.key = temp  # --> запишем найденный элемент вместо того, что надо было удалить
            self.data = temp2

        return self

    def search_min(self):
        """
        вспомогательная функция для поиска наименьшего элемента (ключа) в дереве, нужна для функции delete
        (если у удаляемого элемента 2 поддерева)
        :return: возвращает ссылку на объект с наименьшим ключом в дереве
        """
        if self.left is not None:
            return self.left.search_min()
        return self

    def search_element(self, key):
        """
        функция для поиска элемента
        :param key: это тот элемент, который мы ищем
        :return: возвращает None если такого элемента нет или возвращает ссылку на объект с искомым ключом (key)
        """
        current = self
        key = int(key)
        while key != current.key:
            if current.left is not None and key < current.key:  # если меньше значит идем в левое поддерево
                current = current.left
            elif current.right is not None and key > current.key:  # если меньше значит идем в левое поддерево
                current = current.right
            else:
                return None
        return current

    def bypass(self, long=0, path=[]):
        """
        Обходит дерево и записывает путь обхода в path.
        Данная функция нужна для отрисовки дерева.
        :param long: глубина дерева (изначально равно нулю)
        :param path: путь обхода, а на первом месте максимальная глубина дерева
        :return: path
        """
        if self.key is None:
            return path
        else:
            a = [self.key, self.data]
            path.append(a)
            if self.left is not None:
                path = self.left.bypass(long+1, path)
                path.append([self.key, None])

            if self.right is not None:
                path = self.right.bypass(long+1, path)
                path.append([self.key, None])

            if long > path[0]:
                path[0] = long

            return path

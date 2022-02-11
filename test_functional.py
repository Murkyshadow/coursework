import sys
from unittest import TestCase
from unittest.mock import MagicMock

from PyQt5 import QtCore
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

from facade import Facade
from gui import MainWindow, DialogInput, DialogDelete, DialogSearch


class FunctionalTest(TestCase):
    def setUp(self):
        self.qapp = QApplication(sys.argv)
        self.facade = Facade('DB_test.db')
        self.window = MainWindow(self.facade)

    def test_add(self):
        btn_add = self.window.ui.btn_add
        QTest.mouseClick(btn_add, QtCore.Qt.MouseButton.LeftButton)     # открывем диалоговое окно, нажав на кнопку
        for window in self.qapp.topLevelWidgets():      # возвращает список ссылок на все открытые окна (главное и диалоговые окна (при чем каждый раз в разном порядке))
            if isinstance(window, DialogInput):     # проверяем принадлежит ли открытое окно классу DialogInput
                dialog = window
                break
        else:
            self.fail()

        dialog.key_input.setValue(10)
        dialog.data_input.setText("1234")         # записываем данные в поля
        self.facade.insert_value = MagicMock()
        QTest.mouseClick(dialog.btn_insert, QtCore.Qt.MouseButton.LeftButton)       # и пытаемся их добавить, нажав на кнопку
        self.facade.insert_value.assert_called_with(10, "1234")                # проверяем: была ли функция вызвана с записанными данными

    def test_delete(self):
        self.facade.insert_value(10, '1231421')
        btn_delete = self.window.ui.btn_delete
        QTest.mouseClick(btn_delete, QtCore.Qt.MouseButton.LeftButton)
        for window in self.qapp.topLevelWidgets():
            if isinstance(window, DialogDelete):
                dialog = window
                break
        else:
            self.fail()

        dialog.input_key.setValue(10)
        self.facade.delete_value = MagicMock()
        QTest.mouseClick(dialog.btn_remove, QtCore.Qt.MouseButton.LeftButton)
        self.facade.delete_value.assert_called_with(10)

        self.facade.insert_value(10, '1231421')
        self.facade.insert_value(7, '1231421')
        self.facade.insert_value(14, '1231421')

        self.window.dialog.del_all = MagicMock()
        QTest.mouseClick(dialog.btn_remove_all, QtCore.Qt.MouseButton.LeftButton)
        self.window.dialog.del_all.assert_called()

    def test_save(self):
        btn_save = self.window.ui.btn_save
        self.facade.save_data = MagicMock()
        QTest.mouseClick(btn_save, QtCore.Qt.MouseButton.LeftButton)
        self.facade.save_data.assert_called()

    def test_search(self):
        self.facade.insert_value(10, '1231421')
        btn_contains = self.window.ui.btn_contains
        QTest.mouseClick(btn_contains, QtCore.Qt.MouseButton.LeftButton)
        for window in self.qapp.topLevelWidgets():
            if isinstance(window, DialogSearch):
                dialog = window
                break
        else:
            self.fail()

        dialog.input_key.setValue(10)
        self.facade.search_element_in_tree = MagicMock()
        QTest.mouseClick(dialog.btn_find, QtCore.Qt.MouseButton.LeftButton)
        self.facade.search_element_in_tree.assert_called_with(10)

    def tearDown(self) -> None:   # закрывает окно после остановки проекта
        self.qapp.deleteLater()

if __name__ == '__main__':
    pass
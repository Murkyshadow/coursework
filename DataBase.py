import sqlite3
import logging
logging.basicConfig(level=logging.INFO)
# logging.disable(logging.INFO)


class DataBase:
    """
    класс с функциями дли взаимодействия с базой данных
    """
    def __init__(self, name):
        """
        создает базу данных
        :param name: имя базы данных
        """
        self.db = sqlite3.connect(f"{name}")
        sql = self.db.cursor()
        sql.execute("""CREATE TABLE IF NOT EXISTS Tree ( 
            key integer, 
            data TEXT
        )""")
        self.db.commit()
        sql.close()

    def get_from_db(self):
        """
        Возвращает все значения из базы данных в переменной data
        :return: data
        """
        sql = self.db.cursor()
        data = [value for value in sql.execute(f"SELECT * FROM Tree")]
        if not data:
            logging.log(logging.INFO, ' база данных пуста')
        sql.close()
        return data

    def del_all(self):
        """
        Вспомогательная функция для save_all.
        Удаляет все данные в базе данных.
        :return: None
        """
        cur = self.db.cursor()
        cur.execute("DELETE from Tree")
        self.db.commit()

    def db_insert(self, key, data):
        """
        функция для вставки данных в базу данных
        :param key: ключ, который вставляем в базу данных
        :param data: данные, которые вставляем в базу данных
        :return: None
        """
        cur = self.db.cursor()
        cur.execute("INSERT INTO Tree VALUES (?,?)", (key, data))
        self.db.commit()
        cur.close()

    def save_all(self, path):
        """
        Переписывает все старые данные на новые - удаляет данные и записывает текущие
        :param path: путь обхода структуры данных
        :return: None
        """
        self.del_all()
        for val in path:
            if val[1] is not None:
                self.db_insert(val[0], val[1])

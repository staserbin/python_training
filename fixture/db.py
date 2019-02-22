import mysql.connector
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    # метод для загрузки списка групп из БД
    def get_group_list(self):
        list = []
        # cursor - специальный объект, который делает запросы и получает их результаты
        cursor = self.connection.cursor()
        try:
            # cursor.execute() - чтение данных из БД
            cursor.execute("select group_id, group_name, group_header, group_footer from table_groups")
            # получаем результаты сделанного запроса
                # 2-й способ получения всех данных: results = cursor.fetchall()
            for row in cursor:
                (id, name, header, footer) = row
                # id=str(id) - приводим значение id к типу str(строка)
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


    def get_contacr_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='NULL'")
            for row in cursor:
                (id, firstname,lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()

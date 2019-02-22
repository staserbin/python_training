# тест на проверку соответствия данных из пользовательского интерфейса и из БД

from model.group import Group
from timeit import timeit


def test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1))

    # name=group.name.strip() - будут удаляться лишние пробелы в начале и в конце
    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    # применяем ко всем объектам загруженным из БД функцию clean
    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    assert False  # sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

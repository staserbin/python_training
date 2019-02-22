# ИСТОЧНИК СЛУЧАЙНЫХ ТЕСТОВЫХ ДАННЫХ

from model.group import Group
import random
import string


# генератор случайных тестовых данных
def random_string(prefix, maxlen):
    # символы, которые мы будем использовать в случайной строке / " "*10 - добавляем 10 пробелов
    symbols = string.ascii_letters + string.digits + " " * 10
    # случайным образом выбирает символ из заданной строки
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# Data Test Driven - когда мы отделяем тестовые данные от сценария и многократно прогоняем одни и те же тестовые сценарии на разных данных

# 1-й способ
# первый объект Group содержит маленький список, содержащий тестовый набор с путыми строками
testdata = [Group(name="", header="", footer="")] + [
# random_string("name", 10) - генерируем случайную строку, которая начинается с префикса name и содержит не более 10 случайных символов
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
# будет сгенерирован объект Group со случайными данными 5 раз
    for i in range(5)
 ]

# 2-й способ
# создаем генератор комбинаций значений из пустых строк и строк со случайными данными.
#testdata = [
#    Group(name=name, header=header, footer=footer)
#    for name in ["", random_string("name", 10)]
#    for header in ["", random_string("header", 20)]
#    for footer in ["", random_string("footer", 20)]
#]
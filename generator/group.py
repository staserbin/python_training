# ГЕНЕРАТОР ГРУПП

from model.group import Group
import random
import string
import os.path
import jsonpickle
import getopt
import sys


# Читаем опции из командной строки
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
# Проводим анализ параметров
n = 5
f = "data/groups.json"

# Управляем генератором при помощи указанных опций -n и -f (см. в Parameters конфигурации group.py)
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
# будет сгенерирован объект Group со случайными данными 5 раз (см. выше n = 5)
    for i in range(n)
 ]


# Сохраняем сгенерированные данные в файл
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    #dumps - импортирует сген-ные данные в формат json
    #out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
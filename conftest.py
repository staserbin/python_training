import pytest
from fixture.application import Application
import json
import os.path
import importlib
import jsonpickle
from fixture.db import DbFixture

fixture = None
target = None


# метка фикстуры инициализации
#@pytest.fixture
#def app(request):
#    fixture = Application()
#    fixture.session.login(username="admin", password="secret")
#    request.addfinalizer(fixture.destroy)
#    return fixture



#    def fin():
#        fixture.session.logout()
#        fixture.destroy()


def load_config(file):
    global target
    if target is None:
        # Определяем путь относительно файла conftest.py - указываем путь к файлу, чтобы не быть привязанным в тестах к рабочей директории
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target



@pytest.fixture
def app(request):
    global fixture
#    global target
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
#    if target is None:
#        # Определяем путь относительно файла conftest.py - указываем путь к файлу, чтобы не быть привязанным в тестах к рабочей директории
#        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
#        with open(config_file) as f:
#            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture

#для работы с Базой Данных
@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")




# метка фикстуры финализации (браузер запускается один раз для всей сессии, всех тестов)
#@pytest.fixture(scope="session", autouse=True)
#def stop(request):
#    def fin():
#        fixture.session.ensure_logout()
#        fixture.destroy()
#    request.addfinalizer(fin)
#    return fixture


# добавляет доп.параметры, которые можно указать при запуске pytest из командной строки и в последствии можем получить
# значения, переданные в этом параметре
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")

# для запуска тестов из терминала:
# F:\workspace\tests\python_training>py.test test\test_del_group.py
# выбираем другой браузер:
# F:\workspace\tests\python_training>py.test --browser=chrome_test\test_del_group.py


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            # как только встретилась фикстура "data_", мы загружаем тестовые данные из модуля, у которого название
            # как у фикстуры, только обрезанное - 5 символов нужно удалить
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    # указываем имя импортируемого модуля "data." и название модуля, который мы хотим импортировать.
    # после импорта берем из него "testdata"
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())

from selenium import webdriver
from fixture.contact import ContactHelper
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wb = webdriver.Firefox()
        elif browser == "chrome":
            self.wb == webdriver.Chrome()
        elif browser == "ie":
            self.wb == webdriver.Ie()
        else:
            # Выброс исключения - выполнения кода в этом месте будет аварийно прервано,
            # но оно будет перехвачено конструкцией try в def is_valid()
            raise ValueError("Unrecognized browser %s" % browser)
#        self.wb.implicitly_wait(5)   -- на локальном сервере в ожидании/задержке нет смысла, т.к. все элементы находятся на локальном компьютере
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        wb = self.wb
        wb.get(self.base_url)

    def is_valid(self):
        try:
            self.wb.current_url()
            return True
        except:
            return False

    def destroy(self):
        self.wb.quit()

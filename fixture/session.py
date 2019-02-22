class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wb = self.app.wb
        self.app.open_home_page()
        wb.find_element_by_name("user").click()
        wb.find_element_by_name("user").clear()
        wb.find_element_by_name("user").send_keys(username)
        wb.find_element_by_name("pass").click()
        wb.find_element_by_name("pass").clear()
        wb.find_element_by_name("pass").send_keys(password)
        wb.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='PASSWORD:'])[1]/following::input[2]").click()

    def logout(self):
        wb = self.app.wb
        wb.find_element_by_link_text("LOGOUT").click()

    def is_logged_in(self):
        wb = self.app.wb
        return len(wb.find_elements_by_link_text("LOGOUT")) > 0

    def is_logged_in_as(self, username):
        wb = self.app.wb
        return self.get_logged_user() == username

    def get_logged_user(self):
        wb = self.app.wb
        return wb.find_element_by_xpath("//div/div[1]/form/b").text[1:-1]


    def ensure_logout(self):
        wb = self.app.wb
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        wb = self.app.wb
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
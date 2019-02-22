from  model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wb = self.app.wb
        if text is not None:
            wb.find_element_by_name(field_name).click()
            wb.find_element_by_name(field_name).clear()
            wb.find_element_by_name(field_name).send_keys(text)

    contact_cache = None

    @property
    def get_contact_list(self):
        if self.contact_cache is None:
            wb = self.app.wb
            self.app.open_home_page()
            self.contact_cache = []
            for row in wb.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                # all_phones = cells[5].text.splitlines()                                              # splitlines - делит строки (текст) в столбце под номером 5
                #self.contact_cache.append(
                #    Contact(firstname=firstname, lastname=lastname, id=id,
                #    homephone = all_phones[0], mobilephone = all_phones[1],
                #                                             workphone = all_phones[2], secondaryphone = all_phones[3]))
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_homepage=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wb = self.app.wb
        self.app.open_home_page()
        row = wb.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wb = self.app.wb
        self.app.open_home_page()
        row = wb.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_to_edit_by_index(index)
        wb = self.app.wb
        self.open_contact_to_edit_by_index(index)
        firstname = wb.find_element_by_name("firstname").get_attribute("value")
        lastname = wb.find_element_by_name("lastname").get_attribute("value")
        id = wb.find_element_by_name("id").get_attribute("value")
        homephone = wb.find_element_by_name("home").get_attribute("value")
        workphone = wb.find_element_by_name("work").get_attribute("value")
        mobilephone = wb.find_element_by_name("mobile").get_attribute("value")
        #faxphone = wb.find_element_by_name("fax").get_attribute("value")
        secondaryphone = wb.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wb = self.app.wb
        self.open_contact_view_by_index(index)
        wb.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)









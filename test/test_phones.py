import re          # пакет для работы с регулярными выражениями

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):                              # данной функцией мы заменяем все символы, которые могут нам помешать при проверке
    return re.sub("[() -]", "", s)         # ("что надо заменять", "на что надо заменять", где заменять)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",   #после отработки map() фильтруем и избавляемся от пустых строк. (!=)- оставляем все не пустые строки
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,  # к пустому значению применять ф-ю clear() нельзя, поэтому фильтруем по None
                                       [contact.homephone, contact.workphone, contact.mobilephone, contact.secondaryphone]))))  # map(lambda, значение) - при его помощи можно применить ко всем значениям
from model.group import Group
#import pytest
#from data.groups import testdata
# Чтобы тестировать на фиксированных (constant) данных:
#from data.add_group import constant as testdata



def test_add_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
#    old_groups = app.group.get_group_list()
    app.group.create(group)
    # ХЭШирование при помощи app.group.count()
#    assert len(old_groups) + 1 == app.group.count()
    new_groups = db.get_group_list()
#    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)












# метка для тестового фреймворка, чтобы он передавал данные в тест
#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
#def test_add_group(app, group):
#    old_groups = app.group.get_group_list()
#    app.group.create(group)
#    # ХЭШирование при помощи app.group.count()
#    assert len(old_groups) + 1 == app.group.count()
#    new_groups = app.group.get_group_list()
#    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_add_empty_group(app):
#    old_groups = app.group.get_group_list()
#    group = Group(name="", header="", footer="")
#    app.group.create(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) + 1 == len(new_groups)
#    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

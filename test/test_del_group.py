from model.group import Group
#from random import randrange
import random
import allure


@allure.step("Deleting groups")
def test_delete_some_group(app, db, check_ui):
#    if app.group.count() == 0:
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
#   old_groups = app.group.get_group_list()
# поиск нужной группы по идентификатору
    group = random.choice(old_groups)
#    index = randrange(len(old_groups))
#    app.group.delete_group_by_index(index)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
#    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    # take a list old_groups and delete from it all elements from 0 to 1 - delete one element
#    old_groups[index:index+1] = []
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert new_groups == app.group.get_group_list()
#        assert sorted(new_groups, key=Group.id_or_max) == app.group.get_group_list(), key=Group.id_or_max
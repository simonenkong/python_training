__author__ = 'Nataly'
from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="not enough groups"))
    old_groups = app.group.get_groups_list()
    app.group.delete_first_group()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[0:1] = []
    assert old_groups == new_groups


def test_delete_ith_group(app, i=2):
    if app.group.count() < i:
        for j in range(i - app.group.count()):
            app.group.create(Group(name="not enough groups"))
    old_groups = app.group.get_groups_list()
    app.group.delete_group_by_number(i)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[i-1:i] = []
    assert old_groups == new_groups

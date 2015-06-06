__author__ = 'Nataly'
from model.group import Group
from random import randrange

def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="not enough groups"))
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups


def test_delete_ith_group(app, i=2):
    if app.group.count() < i:
        for j in range(i - app.group.count()):
            app.group.create(Group(name="not enough groups"))
    old_groups = app.group.get_groups_list()
    app.group.delete_group_by_index(i)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[i:i+1] = []
    assert old_groups == new_groups

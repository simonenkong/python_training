__author__ = 'Nataly'
from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="not enough groups"))
    app.group.delete_first_group()


def test_delete_ith_group(app, i=2):
    while app.group.count() < i:
        app.group.create(Group(name="not enough groups"))
    app.group.delete_group_by_number(i)

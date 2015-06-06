__author__ = 'Nataly'

from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="not enough groups"))
    app.group.edit_first_group(Group(name="edited_name", header="edited_header", footer="edited_footer"))


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="not enough groups"))
    app.group.edit_first_group(Group(name="New name"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="not enough groups"))
    app.group.edit_first_group(Group(header="New header"))


def test_edit_ith_group(app, i=2):
    if app.group.count() < i:
        for j in range(i - app.group.count()):
            app.group.create(Group(name="not enough groups"))
    app.group.edit_group_by_number(Group(name="edited_name", header="edited_header", footer="edited_footer"), i)


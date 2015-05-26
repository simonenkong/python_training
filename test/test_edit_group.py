__author__ = 'Nataly'

from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="edited_name", header="edited_header", footer="edited_footer"))
    app.session.logout()


def test_edit_ith_group(app, i=2):
    app.session.login(username="admin", password="secret")
    app.group.edit_group_by_number(Group(name="edited_name", header="edited_header", footer="edited_footer"), i)
    app.session.logout()

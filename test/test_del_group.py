__author__ = 'Nataly'


def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()


def test_delete_ith_group(app, i=2):
    app.session.login(username="admin", password="secret")
    app.group.delete_group_by_number(i)
    app.session.logout()
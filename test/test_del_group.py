__author__ = 'Nataly'


def test_delete_first_group(app):
    app.group.delete_first_group()


def test_delete_ith_group(app, i=2):
    app.group.delete_group_by_number(i)

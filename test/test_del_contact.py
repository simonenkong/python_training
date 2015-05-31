__author__ = 'Nataly'


def test_delete_first_contact(app):
    app.contact.delete_first_contact()


def test_delete_contact_by_number(app, i=2):
    app.contact.delete_contact_by_number(i)

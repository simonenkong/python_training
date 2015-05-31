__author__ = 'Nataly'
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="not enough contacts"))
    app.contact.delete_first_contact()


def test_delete_contact_by_number(app, i=2):
    while app.contact.count() < i:
        app.contact.add_new(Contact(firstname="not enough contacts"))
    app.contact.delete_contact_by_number(i)

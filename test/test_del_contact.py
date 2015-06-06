__author__ = 'Nataly'
from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="not enough contacts"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index-1:index] = []
    assert old_contacts == new_contacts


def test_delete_contact_by_number(app, i=2):
    if app.contact.count() < i:
        for j in range(i - app.contact.count()):
            app.contact.add_new(Contact(firstname="not enough contacts"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_contact_by_index(i)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[i-1:i] = []
    assert old_contacts == new_contacts

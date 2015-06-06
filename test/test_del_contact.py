__author__ = 'Nataly'
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="not enough contacts"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


def test_delete_contact_by_number(app, i=2):
    if app.contact.count() < i:
        for j in range(i - app.contact.count()):
            app.contact.add_new(Contact(firstname="not enough contacts"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_contact_by_number(i)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[i-1:i] = []
    assert old_contacts == new_contacts

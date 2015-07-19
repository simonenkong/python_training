__author__ = 'Nataly'

from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a non-empty contact list')
def non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(firstname="some name"))
    return db.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@given('a contact with <firstname> and <lastname>')
def new_contact(firstname, lastname):
    return Contact(firstname=firstname, lastname=lastname)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.add_new(new_contact)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@when('I change the contact name to <new_name>')
def change_contact_name(app, random_contact, new_name):
    edited_contact = random_contact
    edited_contact.firstname = new_name
    app.contact.edit_contact_by_id(edited_contact, random_contact.id)


@then('the new contact list is equal to the old list without the deleted contact')
def verify_contact_deleted(app, db, random_contact, non_empty_contact_list):
    old_contacts = non_empty_contact_list
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_list = contact_list
    new_list = db.get_contact_list()
    old_list.append(new_contact)
    assert sorted(old_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)


@then('the new contact list is equal to the old list')
def verify_contact_edited(db, contact_list):
    old_list = contact_list
    new_list = db.get_contact_list()
    assert sorted(old_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)
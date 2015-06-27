__author__ = 'Nataly'

from model.contact import Contact
import random

def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(firstname="not enough contacts"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    edited_contact = Contact(firstname="edited name", middlename="edited middle name", lastname="edited last name", nickname="edited nick",
                         title="edited title1", company="edited company1", address="edited address1",
                         home="edited home1", mobile="edited mobile1", work="edited work1", fax="edited fax1", email="edited simonenkong@company1", email2="edited simon2@campany2",
                         email3="editedsimon3@company3", homepage="edited homepage1", byear="1889", ayear="1997", address2="edited address2", phone2="edited phone2", notes="edited notes2")
    edited_contact.id = contact.id
    app.contact.edit_contact_by_id(edited_contact, contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(edited_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)

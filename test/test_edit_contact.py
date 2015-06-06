__author__ = 'Nataly'

from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="not enough contacts"))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="edited name", middlename="edited middle name", lastname="edited last name", nickname="edited nick",
                         title="edited title1", company="edited company1", address="edited address1",
                         home="edited home1", mobile="edited mobile1", work="edited work1", fax="edited fax1", email="edited simonenkong@company1", email2="edited simon2@campany2",
                         email3="editedsimon3@company3", homepage="edited homepage1", byear="1889", ayear="1997", address2="edited address2", phone2="edited phone2", notes="edited notes2")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_contact_by_number(app, i=2):
    if app.contact.count() < i:
        for j in range(i - app.contact.count()):
            app.contact.add_new(Contact(firstname="not enough contacts"))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="edited name", middlename="edited middle name", lastname="edited last name", nickname="edited nick",
                         title="edited title1", company="edited company1", address="edited address1",
                         home="edited home1", mobile="edited mobile1", work="edited work1", fax="edited fax1", email="edited simonenkong@company1", email2="edited simon2@campany2",
                         email3="editedsimon3@company3", homepage="edited homepage1", byear="1889", ayear="1997", address2="edited address2", phone2="edited phone2", notes="edited notes2")
    contact.id = old_contacts[i-1].id
    app.contact.edit_contact_by_number(contact, i)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[i-1] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="Наталия", middlename="Георгиевна", lastname="Симоненко", nickname="simon",
                         title="title1", company="company1", address="address1",
                         home="home1", mobile="mobile1", work="work1", fax="fax1", email="simonenkong@company1", email2="simon2@company2",
                         email3="simon3@company3", homepage="homepage1", byear="1989", ayear="2007", address2="address2", phone2="phone2", notes="notes2")
    app.contact.add_new(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


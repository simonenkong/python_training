# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    symbols = string.digits + " "*5 + "()+-"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + '_' + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + '@' + \
        "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + '.com'


def random_year(startyear):
    return str(startyear + random.randint(0, 50))


def random_day():
    return random.randint(1, 31)


def random_month():
    return random.randint(1, 12)

testdata = [Contact(firstname=random_string('firstname', 10), middlename=random_string('middlename', 10),
            lastname=random_string('lastname', 10), nickname=random_string('nickname', 10),
            title=random_string('title', 10), company=random_string('company', 10),
            address=random_string('address', 10), home=random_number(10),
            mobile=random_number(10), work=random_number(10),
            fax=random_number(10), email=random_email('email', 10),
            email2=random_email('email2', 10), email3=random_email('email3', 10),
            homepage=random_string('homepage', 10), byear=random_year(1950),
            bday=random_day(), bmonth=random_month(),
            aday=random_day(), amonth=random_month(),
            ayear=random_year(2000), address2=random_string('address2', 10),
            phone2=random_number(10), notes=random_string('notes', 10))
    for i in range(3)
]

@pytest.mark.parametrize('contact', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.add_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


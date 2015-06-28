__author__ = 'Nataly'

import re
from model.contact import Contact


def test_all_fields_of_all_contacts_on_home_page(app, db):
    contacts_from_home_page = sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert contacts_from_home_page == contacts_from_db  # checks ids, firstnames and lastnames

    for n in range(len(contacts_from_home_page)):
        assert contacts_from_home_page[n].address == contacts_from_db[n].address
        assert contacts_from_home_page[n].all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[n])
        assert contacts_from_home_page[n].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[n])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None,
                                    [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
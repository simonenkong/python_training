__author__ = 'Nataly'

from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="not enough contacts"))
    app.contact.edit_first_contact(Contact(firstname="edited name", middlename="edited middle name", lastname="edited last name", nickname="edited nick",
                         title="edited title1", company="edited company1", address="edited address1",
                         home="edited home1", mobile="edited mobile1", work="edited work1", fax="edited fax1", email="edited simonenkong@company1", email2="edited simon2@campany2",
                         email3="editedsimon3@company3", homepage="edited homepage1", byear="1889", ayear="1997", address2="edited address2", phone2="edited phone2", notes="edited notes2"))


def test_edit_contact_by_number(app, i=2):
    if app.contact.count() < i:
        for j in range(i - app.contact.count()):
            app.contact.add_new(Contact(firstname="not enough contacts"))
    app.contact.edit_contact_by_number(Contact(firstname="edited name", middlename="edited middle name", lastname="edited last name", nickname="edited nick",
                         title="edited title1", company="edited company1", address="edited address1",
                         home="edited home1", mobile="edited mobile1", work="edited work1", fax="edited fax1", email="edited simonenkong@company1", email2="edited simon2@campany2",
                         email3="editedsimon3@company3", homepage="edited homepage1", byear="1889", ayear="1997", address2="edited address2", phone2="edited phone2", notes="edited notes2"), i)

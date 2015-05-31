# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.add_new(Contact(firstname="Наталия", middlename="Георгиевна", lastname="Симоненко", nickname="simon",
                         title="title1", company="company1", address="address1",
                         home="home1", mobile="mobile1", work="work1", fax="fax1", email="simonenkong@company1", email2="simon2@campany2",
                         email3="simon3@company3", homepage="homepage1", byear="1989", ayear="2007", address2="address2", phone2="phone2", notes="notes2"))



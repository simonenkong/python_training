__author__ = 'Nataly'
from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    groups = db.get_contact_list()
    for group in groups:
        print(group)
    print(len(groups))
finally:
    db.destroy()

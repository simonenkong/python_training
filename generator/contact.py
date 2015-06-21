# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import getopt
import sys
import json
import os.path

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))

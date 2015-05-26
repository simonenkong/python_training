__author__ = 'Nataly'


def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()

def test_delete_contact_by_unmber(app, i=2):
    app.session.login(username="admin", password="secret")
    app.contact.delete_contact_by_number(i)
    app.session.logout()
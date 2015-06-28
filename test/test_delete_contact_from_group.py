__author__ = 'Nataly'
from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_from_group(app, orm):
    # get groups and contacts
    group_list = orm.get_group_list()
    contact_list = orm.get_contact_list()
    # if no groups => add group
    if len(group_list) == 0:
        app.group.create(Group(name="not enough groups"))
    # choose random target group
    group_list = orm.get_group_list()
    target_group = random.choice(group_list)
    # if no contacts  => add contact
    if len(contact_list) == 0:
        app.contact.add_new(Contact(firstname="not enough contacts"))
    # if no contacts in target group => add one to target group
    if len(orm.get_contacts_in_group(target_group)) == 0:
        contact = random.choice(orm.get_contacts_not_in_group(target_group))
        app.contact.add_contact_to_group(contact, target_group)
    contact = random.choice(orm.get_contacts_in_group(target_group))
    old_contacts_in_target_group = orm.get_contacts_in_group(target_group)
    app.contact.delete_contact_from_group(contact, target_group)
    new_contacts_in_target_group = orm.get_contacts_in_group(target_group)
    old_contacts_in_target_group.remove(contact)
    assert sorted(old_contacts_in_target_group, key=Contact.id_or_max) == sorted(new_contacts_in_target_group, key=Contact.id_or_max)



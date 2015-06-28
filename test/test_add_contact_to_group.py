__author__ = 'Nataly'
from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, orm):
    # get groups and contacts
    group_list = orm.get_group_list()
    contact_list = orm.get_contact_list()
    # if no groups => add group
    if len(group_list) == 0:
        app.group.create(Group(name="not enough groups"))
    # choose random target group
    group_list = orm.get_group_list()
    target_group = random.choice(group_list)
    # if no contacts or no contacts not in this group => add contact
    if len(contact_list) == 0 or len(orm.get_contacts_not_in_group(target_group)) == 0:
        app.contact.add_new(Contact(firstname="not enough contacts"))
    # choose random contact not in target group
    contact = random.choice(orm.get_contacts_not_in_group(target_group))
    old_contacts_in_target_group = orm.get_contacts_in_group(target_group)
    app.contact.add_contact_to_group(contact, target_group)
    new_contacts_in_target_group = orm.get_contacts_in_group(target_group)
    old_contacts_in_target_group.append(contact)
    assert sorted(old_contacts_in_target_group, key=Contact.id_or_max) == sorted(new_contacts_in_target_group, key=Contact.id_or_max)



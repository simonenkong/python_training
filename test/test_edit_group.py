__author__ = 'Nataly'

from model.group import Group
import random

def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="not enough groups"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    edited_group = Group(name="edited_name", header="edited_header", footer="edited_footer")
    edited_group.id = group.id
    app.group.edit_group_by_id(edited_group, group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(edited_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)

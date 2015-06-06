__author__ = 'Nataly'

from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="not enough groups"))
    old_groups = app.group.get_groups_list()
    group = Group(name="edited_name", header="edited_header", footer="edited_footer")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="not enough groups"))
#     old_groups = app.group.get_groups_list()
#     app.group.edit_first_group(Group(name="New name"))
#     new_groups = app.group.get_groups_list()
#     assert len(old_groups) == len(new_groups)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="not enough groups"))
#     old_groups = app.group.get_groups_list()
#     group = Group(name="edited_name", header="edited_header", footer="edited_footer")
#     group.id = old_groups[0].id
#     app.group.edit_first_group(Group(header="New header"))
#     new_groups = app.group.get_groups_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_edit_ith_group(app, i=2):
    if app.group.count() < i:
        for j in range(i - app.group.count()):
            app.group.create(Group(name="not enough groups"))
    old_groups = app.group.get_groups_list()
    group = Group(name="edited_name", header="edited_header", footer="edited_footer")
    group.id = old_groups[i-1].id
    app.group.edit_group_by_number(Group(name="edited_name", header="edited_header", footer="edited_footer"), i)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[i-1] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

from model.group import Group
#from random import randrange
import random

def test_modify_group_name(app,db,check_ui):
    if len (db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
#    index = randrange(len(old_groups))
    newgroup = Group(name="New group123")
    newgroup.id = group.id
    app.group.modify_group_by_id(group.id,newgroup)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(newgroup)
#    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max()) == sorted(app.group.get_group_list(), key=Group.id_or_max())


#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    app.group.modify_first_group(Group(header="Old header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)



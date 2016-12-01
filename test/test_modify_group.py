from model.group import Group

def test_modify_group_name(app):
    #app.session.login(username="admin", password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="Old group"))
    #app.session.logout()

def test_modify_group_header(app):
          #app.session.login(username="admin", password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(header="Old header"))
          #app.session.logout()


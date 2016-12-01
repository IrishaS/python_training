from model.contact import Contact

def test_modify_contact_firstname(app):
    #app.session.login(username="admin", password="secret")
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(firstname="Vadim"))
    #app.session.logout()

def test_modify_contact_lastname(app):
    #app.session.login(username="admin", password="secret")
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(lastname="Ivanov"))
    #app.session.logout()
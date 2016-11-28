from model.contact import Contact

def test_delete_contact(app):
    #app.session.login(username="admin", password="secret")
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.delete_contact()
    #app.session.logout()



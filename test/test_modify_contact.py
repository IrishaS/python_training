from model.contact import Contact
import random

def test_modify_contact_firstname(app,db,check_ui):
    if len (db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
#    index = randrange(len(old_contacts))
    newcontact = Contact(firstname="Julia")
    newcontact.id = contact.id
    newcontact.lastname = contact.lastname
    app.contact.modify_contact_by_id(contact.id,newcontact)
#    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
#    old_contacts[index] = contact
    old_contacts.remove(contact)
    old_contacts.append(newcontact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max()) == sorted(app.contact.get_group_list(),
                                                                   key=Contact.id_or_max())


def test_modify_contact_lastname(app,db,check_ui):
    if len (db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    newcontact = Contact(lastname="Petrov")
    newcontact.id = contact.id
    newcontact.firstname = contact.firstname
    app.contact.modify_contact_by_id(contact.id,newcontact)
#    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(newcontact)
#    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max()) == sorted(app.contact.get_group_list(),
                                                                   key=Contact.id_or_max())


# -*- coding: utf-8 -*-
#import pytest

#from fixture.application import Application
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

testdata = [Contact(firstname="",lastname="")]+[
    Contact(firstname=random_string ("Fname",10), lastname=random_string ("Lname",15))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_test_add_contact_new2(app,contact):
    old_contacts = app.contact.get_contact_list()
#    contact = Contact (firstname="Irisha1", lastname="Silkina", company="Tele2", address="SPb", homephone="1452367",
#                               mobilephone="+79814442233", email="Tele2@mail.ru",
#                               #day="7", month="6",
#                              year="1980", address2="Moscou")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

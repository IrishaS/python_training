# -*- coding: utf-8 -*-
#import pytest

#from fixture.application import Application
from model.contact import Contact


#@pytest.fixture
#def app(request):
    #fixture = Application()
    #request.addfinalizer(fixture.destroy)
    #return fixture

def test_test_add_contact_new2(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Irisha1", lastname="Silkina", company="Tele2", address="SPb", homephone="1452367",
                               mobile="+79814442233", email="Tele2@mail.ru",
                               #day="7", month="6",
                               year="1980", address2="Moscou"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


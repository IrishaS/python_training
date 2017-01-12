import re

def test_addresses_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.address == contact_from_edit_page.address

def clear(s):
    return re.sub("[() -]", "",s)

#def merge_addresses_like_on_home_page(contact):
#    return "\n".join(filter(lambda x: x != "",
#                            map (lambda x: clear (x) ,
#                                 filter(lambda x: x is not None,
#                                        [contact.address, contact.address2]))))
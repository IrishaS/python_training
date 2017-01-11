from model.contact import Contact

class ContactHelper:

    def __init__(self,app):
        self.app = app


    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % contact.day).is_selected():
            #wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % contact.day).click()
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % contact.month).is_selected():
            #wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % contact.month).click()
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value_contact("firstname",contact.firstname)
        self.change_field_value_contact("lastname", contact.lastname)
        self.change_field_value_contact("company", contact.company)
        self.change_field_value_contact("address", contact.address)
        self.change_field_value_contact("home", contact.homephone)
        self.change_field_value_contact("mobile", contact.mobile)
        self.change_field_value_contact("email", contact.email)
        self.change_field_value_contact("byear", contact.year)
        self.change_field_value_contact("address2", contact.address2)


    def change_field_value_contact(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
#        self.open_contact_page()
#        self.select_contact_by_index(index)
#        # open modification
#        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.open_contact_to_edit_by_index(index)
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def open_contact_to_edit_by_index(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("http://localhost/addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr"):
                name = element.get_attribute("name")
                if name =='entry':
                    lastname = element.find_elements_by_tag_name("td")[1].text
                    firstname = element.find_elements_by_tag_name("td")[2].text
                    id = element.find_element_by_name("selected[]").get_attribute("value")
                    self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)


from sys import maxsize

class Contact:

    def __init__(self, firstname = None, lastname = None, id = None, company = None, address = None, homephone = None,
                 mobilephone = None, workphone = None, secondaryphone = None,
                 email = None, email2 = None, email3 = None,
                 #day,
                       #month,
                 year = None, address2 = None,
                 all_phones_from_home_page = None,
                 all_emails_from_home_page = None):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.address = address
        self.address2 = address2
        #self.day = int(day) + 2
        #self.month = int(month) + 1
        self.year = year
        self.address2 = address2
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s %s " % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
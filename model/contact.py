from sys import maxsize

class Contact:

    def __init__(self, firstname = None, lastname = None, company = None, address = None, homephone = None,
                 mobile = None, email = None,
                 #day,
                       #month,
                 year = None, address2 = None,id = None):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobile = mobile
        self.email = email
        #self.day = int(day) + 2
        #self.month = int(month) + 1
        self.year = year
        self.address2 = address2
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
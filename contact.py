class Contact:

    def __init__(self, firstname, lastname, company, address, homephone, mobile, email, day,
                       month, year, address2):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobile = mobile
        self.email = email
        self.day = int(day) + 2
        self.month = int(month) + 1
        self.year = year
        self.address2 = address2
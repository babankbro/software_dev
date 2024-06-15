class Contact:
    all_contact = []
    def __init__(self, name, email):
        self.name = name
        self.email = email   
        self.all_contact.append(self)
        
class AddressHolder:
    def __init__(self, street, city, provine, code):
        self.street = street
        self.street = city
        self.street = provine
        self.street = code
        
class Friend(Contact, AddressHolder):
    def __init__(self, name, email, street, city, provine, code):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, provine, code)
        
f = Friend("Nick", "nick@gmail.com", "Karset Somboon", "Kalasin",
           "Kalasin", "46000")
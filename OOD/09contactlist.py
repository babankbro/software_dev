class ContactList(list):
    
    def search(self, name):
        match_contact = []
        for contact in self:
            if name in contact.name:
                match_contact.append(contact)
        return match_contact

class Contact:
    all_contacts = ContactList()
    
    def __init__(self, name):
        self.name = name
        self.all_contacts.append(self)
        
    def __str__(self):
        return f"Name:{self.name}"
    

c1 = Contact( "John A" )
c2 = Contact( "Robert B" )
c3 = Contact( "John Robert C" )
c4 = Contact( "Jone Robert C" )

for x in c1.all_contacts.search( "Robert" ):
    print(x.name)
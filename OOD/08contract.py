class Contact:
    all_contacts = []
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)
        
    def __str__(self):
        return f"Name:{self.name} Email:{self.email}"

class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone
        
    def __str__(self):
        return super().__str__() + f" Phone: {self.phone}"

class Supplier(Contact):
    def order(self, order):
        print( f"Send {order} to {self.name}" )

f1 = Friend("Nick", "nick@gmail.com", "088546213")
f2 = Friend("Bob", "bob@gmail.com", "091111111")
f3 = f2
print(f1)
print(f2)
print(id(f1))
print(id(f2))
print(id(f3))
print(id(f1.all_contacts))
print(id(f2.all_contacts))
print(id(Friend.all_contacts))
s = Supplier("Pizza Hut", "order@gmail.com")
s.order("8 Chicken Wings!")
for p in s.all_contacts:
    print(p)
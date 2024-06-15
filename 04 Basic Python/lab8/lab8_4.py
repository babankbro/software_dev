class Person:
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    
    def display(self):
        print(f"Name:{self.name} , Age: {self.age}" +
              f",Email: {self.email}")
        
    def __str__(self):
        return f"Name:{self.name} , Age: {self.age}" +\
               f",Email: {self.email}"



person1 = Person("Sarayut Gonwirat", 40, "sarayut.go@ksu.ac.th")
person2 = Person("Mr. A", 20, "babankbro@gmail.com")
#person1.display()
#person2.display()
print(person1)
print(person2)

class Person:
    
    def display(self):
        print(f"Name:{self.name} , Age: {self.age}" +
              f",Email: {self.email}")

    


person = Person()
person.name = "Sarayut Gonwirat"
person.age = 30
person.email = "sarayut.go@ksu.ac.th"
person.display()
class Cat:
    
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        
    def meow(self):
        print("Meaw Meaw!")
        
    def display_info(self):
        print(f"Name:{self.name} , Age: {self.age}" +
              f",Breed: {self.breed}")
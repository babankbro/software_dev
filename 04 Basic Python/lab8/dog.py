class Dog:
    
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        
    
    def bark(self):
        print("Hong Hong!")
        
    def display_info(self):
        print(f"Name:{self.name} , Age: {self.age}" +
              f",Breed: {self.breed}")
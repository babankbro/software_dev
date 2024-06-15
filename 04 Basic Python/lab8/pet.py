class Pet:
    
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        
    
    def make_sound(self):
        return "pet makesound"
        
    def display_info(self):
        print(f"Name:{self.name} , Age: {self.age}" +
              f",Breed: {self.breed}")
        

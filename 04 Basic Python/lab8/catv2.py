from pet import *

class Cat(Pet):
    
    def meow(self):
        return "Meow Meow!"
    
    def make_sound(self):
        return f"{self.name}, "+ self.meow()
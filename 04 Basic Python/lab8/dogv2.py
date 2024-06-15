from pet import *

class Dog(Pet):
    
    def bark(self):
        return "Hong Hong!"
    
    def make_sound(self):
        return f"{self.name}, "+ self.bark()
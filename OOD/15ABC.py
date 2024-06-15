from abc import ABC, abstractclassmethod

class A(ABC):
    @abstractclassmethod
    def speak(self):
        print("Un-gu")
       
    @abstractclassmethod 
    def add(self, a, b):
        pass
    
class S(A):
    def speak(self):
        super().speak()
        print("Every Sha la la la Every Wo o wo o")
    
    def add(self, a, b):
        return a + b
    
a = S()
a.speak()
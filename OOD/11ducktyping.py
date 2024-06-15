class Duck:
    def fly(self):
        print("Duck fly!")
        
class Airplane:
    def fly(self):
        print("Airplane fly!")
        
class Whale:
    def swim(self):
        print("Whale swim.")
        
        
def life_off(entity):
    entity.fly()
    
        
d = Duck()
a = Airplane()
w = Whale()

life_off(d)
life_off(a)
life_off(w)


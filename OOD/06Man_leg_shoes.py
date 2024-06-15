class Shoes:
    def __init__(self, size):
        self.size = size

class Leg:
    def __init__(self, length):
        self.length = length

class Man:
    def __init__(self, shoes):
        self.leg = Leg(120)
        self.shoes = shoes

shoes = Shoes(9)
man = Man(shoes)
print(man.leg)
print(man.shoes)
del man
print(shoes)
print(man.leg)

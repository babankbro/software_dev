class Fight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger_names = []
    
    def add_passager(self, name):
        if not self.open_seat() > 0:
            return False
        self.passenger_names.append(name)
        return True
    
    def open_seat(self):
        return self.capacity - len(self.passenger_names)
        
fight = Fight(3)

names = ["Harry", "Ron", "Hermione", "Draco"]
for name in names:
    sucess = fight.add_passager(name)
    if sucess:
        print(f"Add {name} to this fight")
    else:
        print(f"Cannot add {name}!!")

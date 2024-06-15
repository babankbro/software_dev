class HotDog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = "Raw"
        self.codiments = []
    
    def cook(self, time):
        self.cooked_level = self.cooked_level + time
        if self.cooked_level > 8:
            self.cooked_string = "Charcoal"
        elif self.cooked_level > 5:
            self.cooked_string = "Well-Done"
        elif self.cooked_level > 3:
            self.cooked_string = "Medium"  
        else:
            self.cooked_string = "Raw"

    def __str__(self):
        msg = "Hogdog"
        msg = f"{self.cooked_string} {msg}."
        if len(self.codiments) > 0:
            msg += "with "
        for item in self.codiments:
            msg += item + ", "
        msg = msg.strip(", ")
        return msg
    
    def addCodiment(self, codiment):
        self.codiments.append(codiment)


myDog = HotDog()
print(myDog)
print("Cooking hot dog for 4 minutes...")
myDog.cook(4)
print(myDog)
print("Cooking hot dog for 3 minutes...")
myDog.cook(3)
print(myDog)
print("Cooking hot dog for 10 minutes...")
myDog.cook(10)
print(myDog)
myDog.addCodiment("ketchup")
myDog.addCodiment("mustard")
print(myDog)
class Orange:
    def __init__(self, weight, orchard, date_picked):
        self.weight = weight
        self.orchard = orchard
        self.date_picked = date_picked
        
    def pick(self, basket):
        basket.accept(self)
        
    def squeeze(self):
        juice = self.weight * 0.7
        self.weight = self.weight - juice
        return juice
               
    def __str__(self):
        return f"Orange info : {self.weight} lbs picked"+\
               f" on {self.date_picked} from {self.orchard}."

class Basket:
    def __init__(self, location):
        self.location = location
        self.oranges = []
        
    def accept(self, orange):
        self.oranges.append(orange)
        
    def sell(self, customer):
        while self.oranges:
            o = self.oranges.pop()
            customer.purchase(o)

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = ""
        
    def purchase(self, item):
        self.purchase_history += str(item) + "\n"
    
    def get_purchase_history(self):
        return f"{self.name} has purchased:\n + {self.purchase_history}"


basket = Basket( "Margate" )
orange1 = Orange(0.5 , "Sutton" , "2018 09 16" )
orange2 = Orange(0.4 , "Holloway" , "2018 09 17" )
orange3 = Orange(0.3 , "Oldham" , "2018 09 18" )
orange3.squeeze()
customer1 = Customer( "Pooter" )
customer2 = Customer( "Lupin" )


orange1.pick( basket )
orange2.pick( basket )
orange3.pick( basket )
basket.sell(customer1)
basket.sell(customer2)

print(customer1.get_purchase_history())
print(customer2.get_purchase_history())
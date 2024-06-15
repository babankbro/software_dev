class Orange:
    
    def __init__(self, weight, orchard, date_picked):
        self.weight = weight
        self.orchard = orchard
        self.date_picked = date_picked
        
    def __str__(self):
        return f"Orange info : {self.weight} lbs picked"+\
               f" on {self.date_picked} from {self.orchard}."
        
#object , instance 

cheap_orange = Orange(0.08 , "Yiwu" , "2018 12 01" )
print ( cheap_orange )
expensive_orange = Orange(0.12 , "Jinhua" , "2018 11 29" )
print ( expensive_orange )
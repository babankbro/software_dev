class Wallet:
    
    def __init__(self, amount):
        self.money = amount
    
    def deposit(self, amount):
        self.money += amount

    def withdraw(self, amount):
        self.money -= amount
    
    def check(self):
        msg = f"The wallet has {self.money} RMB"
        #print(msg)
        return msg
    
w = Wallet(0)
print(w.check())
w.deposit(1000)
print(w.check())
w.withdraw(500)
print(w.check())
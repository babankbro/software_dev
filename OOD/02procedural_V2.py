
def create(amount):
    return {"money": amount}

def deposit(wallet, amount):
    wallet["money"] += amount
    
def withdraw(wallet, amount):
    wallet["money"] -= amount
    
def check(wallet):
    return f"The wallet has {wallet['money']} RMB"

wallet = create(0)
print(type(wallet))
print(check(wallet))
deposit(wallet, 1000)
print(check(wallet))
withdraw(wallet, 500)
print(check(wallet))
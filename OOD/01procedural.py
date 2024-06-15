money = 0

def deposit(amount):
    global money
    money += amount
    
def withdraw(amount):
    global money
    money -= amount
    
def check():
    global money
    return f"The wallet has {money:2f} RMB"

print(check())
deposit(1000)
print(check())
withdraw(500)
print(check())
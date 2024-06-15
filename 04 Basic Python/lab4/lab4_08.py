def line():
    for j in range(10):
        print("#", end="")
    print()

def block():
    for i in range(5):
        line()
        
block()
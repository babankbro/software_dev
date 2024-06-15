def line(ch, col):
    for j in range(col):
        print(ch, end="")
    print()

def block(ch, row, col):
    for i in range(row):
        line(ch, col)
        
block("o", 4, 7)
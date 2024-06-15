n = int(input("Enter number of rows:"))

for i in range(n):
    print(i, end="")
    for j in range(2*n-1):
        if j < n-1 - i:
            print("o", end="")
        elif j < n + i:
            print("#", end="")
        else:
            print("o", end="")
            
    print()
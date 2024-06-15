row = int(input("Enter number of rows:"))
col = int(input("Enter number of column:"))
print(f"The block of {row} rows and {col} columns.")

for j in range(row):
    for i in range(col):
        print("o", end="")
    print()
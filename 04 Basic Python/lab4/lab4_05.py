def average(x, y, z):
    avg = (x + y + z)/3
    return avg

n1 = float(input("Enter first number:"))
n2 = float(input("Enter second number:"))
n3 = float(input("Enter third number:"))
avg = average(n1, n2, n3)
print(f"The average is {avg:.2f}.")
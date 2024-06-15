def cel_to_fah(c):
    f = c*9/5 + 32   # c = (f-32)*5/9 ,  c*9/5 + 32
    return f

c = float(input("Type in temperature in Celsius:"))
f = cel_to_fah(c)
print(f"That is {f:.2f} degrees in Farentheit.")
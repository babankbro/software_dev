from my_module import average, cel_to_fah, grade, introduce

introduce("Bank", 30, 'red')

f = cel_to_fah(37)
print("The fahrentheit is {f:.2f}.")

g =  grade(37)
print(f"Grade of 37 is {g}.")

avg = average(1, 2, 3)
print(f"The average is {avg:.2f}.")

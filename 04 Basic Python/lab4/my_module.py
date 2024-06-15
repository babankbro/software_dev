def introduce(name, age, color):
    print(f"My name is {name}.")
    print(f"I'm {age} years old.")
    print(f"My favorite color is {color}.")
    print() 


def cel_to_fah(c):
    f = c*9/5 + 32   # c = (f-32)*5/9 ,  c*9/5 + 32
    return f

def average(x, y, z):
    avg = (x + y + z)/3
    return avg

def grade(score):
    if score < 50:
        return "F"
    elif score < 60:
        return "D"
    elif score < 70:
        return "C"
    elif score < 80:
        return "B"
    return 'A'

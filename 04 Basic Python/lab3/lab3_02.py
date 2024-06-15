name = input("Who are you?")
age = int(input("How old are you? "))
if name=="Alice":
    print("Hi, Alice")
else:
    if age <= 12:
        print("You are not Alice, kido.")
    else:
        print("You are neither Alice nor a litte kid.")
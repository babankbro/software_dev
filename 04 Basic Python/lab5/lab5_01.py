#person = ["Sarayut", "red", 30]
#print(person[2])
#json 
print("1.1)")
personal_data = {"name":"Sarayut", "color":"green", "age":30}
print(personal_data)
print()

print("1.2)")
print(personal_data["color"])

print("1.3)")
personal_data["color"] = 'red'
print(personal_data["color"])

print("1.4)")
personal_data["country"] = 'Kalasin'
print(personal_data)

print("1.4)")
del personal_data["color"] 
print(personal_data)
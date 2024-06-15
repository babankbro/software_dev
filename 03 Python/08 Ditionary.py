#telephone = ["191", "1113", "1669", '1112']
telephones = {"police": "191", 
             "google": "1113", 
             "hospital": "1669", 
             "pizza": '1112'}

telephones["supicha"] =  "xxx"

print("Google Tel.", telephones['google'])

name = input("Name: ")
print(f"{name} Tel.", telephones[name])

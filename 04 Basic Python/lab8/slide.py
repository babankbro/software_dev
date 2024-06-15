l = [2, 5, 7, 8]
d = {"name":"Sarayut", 
     'age':25, 
     'color': 'red'}
print(type(l))
print(type(d))

print(l)
print(l[1]) #index 
print(d['age']) #key
for i in range(len(l)):
    print(i, l[i])

for value in l:
    print(value)

print("Dic=======")
for key in d:
    print(key, d[key])
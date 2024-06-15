import pandas as pd
import matplotlib.pyplot as plt

f = open("lab6/DM.csv", 'r')
lines = f.readlines()
DM = []
for i in range(len(lines)):
    line = lines[i]
    line = line.replace("\n", '')
    line = line.replace("\t", '')
    data = line.split(',')
    numbers = []
    for d in data:
        numbers.append(float(d))
    DM.append(numbers)
    
def distane_route(route, DM):
    total = 0
    N = len(route)
    for i in range(N-1):
        current = route[i]
        next_city = route[i+1]
        total += DM[current][next_city]
    current = route[-1]
    next_city = route[0]
    total += DM[current][next_city]
    return total
        
route = [0, 4, 2,  5, 6, 3, 7, 1, 8, 9, 0]
total_distance = distane_route(route, DM)
print("Distance: T1->T5->T3->T6->T7->T4->T8->T2->T9->T10->T1:")
print(total_distance)

df = pd.read_csv("lab6/travel.csv")

lats = df['Lat']
lngs = df['Lng']

ids = []
for i in range(len(lats)):
    ids.append(f"T{i+1}")
print(ids)
plt.scatter(lats, lngs)
for i in range(len(ids)):
    name = ids[i]
    plt.annotate(name, xy=(lats[i], lngs[i]), 
                 xytext=(lats[i]+0.01, lngs[i]+0.01))
plt.plot( lats[route], lngs[route],   color='red')

plt.show()


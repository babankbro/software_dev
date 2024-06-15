import pandas as pd
import matplotlib.pyplot as plt

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
plt.show()
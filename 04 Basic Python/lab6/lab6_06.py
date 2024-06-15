import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("lab6/travel.csv")
print(df)
print()
print(df.columns)
print()
print(df['Name'])
print()
print(df['Lat'])
print("describe")
print(df.describe())
print("info")
df.info()


#plt.scatter(df['Lat'], df['Lng'])
#plt.show()

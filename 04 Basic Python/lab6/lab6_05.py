import matplotlib.pyplot as plt

f = open("lab6/points.txt", 'r')
lines = f.readlines()
xs = []
ys = []
for i in range(len(lines)):
    line = lines[i]
    line = line.replace("\n", "")
    line = line.replace("\ufeff", "")
    points = line.split(',')
    x = int(points[0])
    y = int(points[1])
    xs.append(x)
    ys.append(y)
    #print(line, x, y)
print("Xs:", xs)
print("Ys:", ys)

plt.scatter(xs, ys, color='red')
#plt.plot(xs, ys, color='blue')
plt.show()
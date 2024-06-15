import matplotlib.pyplot as plt

xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ys = [4, 8, 5, 6, 8, 2, 1, 4, 3, 1]

plt.scatter(xs, ys, color='red')
plt.plot(xs, ys, color='blue')
plt.show()
import matplotlib.pyplot as plt

trafic = [1200, 1350, 900, 1500, 1700, 1600, 1800]
CA = [3000, 3300, 2500, 4000, 4500, 4300, 5000]

plt.scatter(trafic, CA, alpha=0.7)
plt.xlabel("Trafic du site")
plt.ylabel("CA")
plt.title("Trafic et CA")
plt.show()

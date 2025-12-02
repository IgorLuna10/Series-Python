import matplotlib.pyplot as plt

revenues = [1500, 1700, 1800, 1900, 2000, 
            2500, 3000, 2800, 5000, 6000, 
            2100, 2200, 2300, 2400, 2500,
            3000, 2900, 5000, 7000, 2000]



plt.hist(revenues, bins=8)
plt.xlabel("Revenues")
plt.ylabel("Nombre de visites")
plt.title("Histogramme des revenues")
plt.show()

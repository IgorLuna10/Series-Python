import csv
import matplotlib.pyplot as plt

def mean_average(revenues, mean):
    result = []

    for i in range(len(revenues)):
        if i < mean -1:
            result.append(None)
        else:
            bloc = revenues[i-mean+1:i+1]
            result.append(sum(bloc) / mean)
    return result


revenues = []
mean = 3

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)  # sauter la ligne d'en-tête
    for ligne in lecteur:
        revenues.append(float(ligne[3]))

moving_mean = mean_average(revenues, mean)

plt.figure(figsize=(10,6))
plt.plot(revenues, marker = "o", label="Daily Revenues", color = "blue")
plt.plot(moving_mean, linestyle="--", marker = "s", label="Moving Average(3 jours)", color = "red")
plt.title("Revenus journaliers et moyenne mobile sur 3 jours")
plt.xlabel("Jours")
plt.ylabel("Revenus")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
import csv
import matplotlib.pyplot as plt

revenues = []

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)  # sauter la ligne d'en-tête
    for ligne in lecteur:
        revenues.append(float(ligne[3]))

mid_point = len(revenues) // 2
week_1_2 = revenues[:mid_point]
week_3_4 = revenues[mid_point:]


plt.boxplot([week_1_2, week_3_4])
plt.ylabel("Revenus (€)")
plt.title("Distribution des revenus : Semaines 1-2 vs 3-4")
plt.xticks([1, 2], ["Semaines 1-2", "Semaines 3-4"])
plt.show()
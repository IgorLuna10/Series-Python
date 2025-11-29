import csv

dates = []
revenus = []

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)  # sauter la ligne d'en-tête
    for ligne in lecteur:
        date = ligne[0]
        trafic = int(ligne[1])
        nb_commandes = int(ligne[2])
        revenu = float(ligne[3])

        dates.append(date)
        revenus.append(revenu)


import matplotlib.pyplot as plt

plt.plot(dates, revenus, marker="o")
plt.xlabel("Date")
plt.ylabel("Revenus")
plt.title("Revenus du site sur 7 jours")
plt.show()
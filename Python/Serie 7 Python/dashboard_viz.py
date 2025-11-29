import csv
import matplotlib.pyplot as plt

dates = []
trafic = []
nb_commandes = []
revenus = []
weekly_revenues = []
week = 7

with open("ventes_journalieres.csv" , "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)
    for ligne in lecteur:
        dates.append(ligne[0])
        trafic.append(int(ligne[1]))
        nb_commandes.append(int(ligne[2]))
        revenus.append(float(ligne[3]))


for i in range (0, len(revenus), week):
    bloc = revenus[i:i+week]
    weekly_revenues.append(sum(bloc))

week_label = [f'w{i+1}' for i in range(len(weekly_revenues))]

plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
plt.plot(dates, trafic, marker="o", color="blue")
plt.title("Trafic quotidien")
plt.ylabel("Visiteurs")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 2)
plt.plot(dates, revenus, marker="o", color="red")
plt.title("Revenus quotidiens")
plt.xlabel("Date")
plt.ylabel("Revenus (€)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 3)
plt.plot(dates, nb_commandes, marker="o", color="green")
plt.title("Nombre de commandes quotidiennes")
plt.xlabel("Date")
plt.ylabel("Nombre de commandes")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 4)
plt.plot(range(1, len(weekly_revenues)+1), weekly_revenues)
plt.xlabel("Semaines")
plt.ylabel("Revenus (€)")
plt.title("Revenus hebdomadaires")
plt.xticks(range(1, len(weekly_revenues)+1), week_label)

plt.suptitle("Tableau de bord e-commerce", fontsize=16)
plt.savefig("dashboard_ecommerce.png", bbox_inches='tight')
plt.tight_layout()
plt.show()
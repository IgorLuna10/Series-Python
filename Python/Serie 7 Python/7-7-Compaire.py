import csv
import matplotlib.pyplot as plt


revenus = []
weekly_revenues = []
week = 7


with open("ventes_journalieres.csv" , "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)
    for ligne in lecteur:
        revenus.append(float(ligne[3]))

for i in range (0, len(revenus), week):
    bloc = revenus[i:i+week]
    weekly_revenues.append(sum(bloc))

week_label = [f'w{i+1}' for i in range(len(weekly_revenues))]

plt.bar(range(1, len(weekly_revenues)+1), weekly_revenues)
plt.xlabel("Semaines")
plt.ylabel("Revenus (€)")
plt.title("Revenus hebdomadaires")
plt.xticks(range(1, len(weekly_revenues)+1), week_label)
plt.show()
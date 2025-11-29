import csv
import matplotlib.pyplot as plt

dates = []
trafic = []
revenus = []

with open("ventes_journalieres.csv" , "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)
    for ligne in lecteur:
        dates.append(ligne[0])
        trafic.append(int(ligne[1]))
        revenus.append(float(ligne[3]))

plt.figure(figsize=(8,6))

plt.subplot(2,1,1)
plt.plot (dates, trafic, marker="o", color="blue")
plt.title("Trafic quotidien")
plt.ylabel("Visiteurs")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

plt.subplot(2,1,2)
plt.plot (dates, revenus, marker="o", color="red")
plt.title("Revenus quotidiens")
plt.xlabel("Date")
plt.ylabel("Revenus (€)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
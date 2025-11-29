prix_ht = float(input("Entrez le prix hors taxe : "))
taux_tva = float(input("Entrez le taux de TVA (en pourcentage) : "))

tva = prix_ht * (taux_tva / 100)
prix_ttc = prix_ht + tva

print(f"Pour un prix HT de {prix_ht}€ et un taux de TVA de {taux_tva}%, le prix TTC est de {prix_ttc}€.")


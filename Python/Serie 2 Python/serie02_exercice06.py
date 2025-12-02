from structures import commandes, total_paid, count_status, total_spent_by_client

# 1. Lire le fichier ligne par ligne.
with open("text.txt", "r", encoding="utf-8") as fichier:
    lignes = fichier.readlines()

# Liste qui contiendra tous les dictionnaires
commandes = []

# Pour chaque ligne du fichier
for ligne in lignes:
    # Enlever les espaces et sauts de ligne
    ligne = ligne.strip()
    
    # Ignorer les lignes vides
    if ligne:
        # Découper la ligne avec split(";")
        parties = ligne.split(";")
        
        # Construire un dictionnaire
        commande = {
            "id": parties[0],
            "client": parties[1],
            "montant": parties[2],
            "statut": parties[3]
        }   
        # Ajouter le dictionnaire dans la liste
        commandes.append(commande)

# Afficher le résultat
print(f"Nombre de commandes : {len(commandes)}")
for cmd in commandes:
    print(cmd)

# 2. Utiliser les fonctions de structures.py pour analyser les données.

print("Total paid:", total_paid(commandes))
print("Status counts:", count_status(commandes))
print("Total spent by client:", total_spent_by_client(commandes))

import os

nom_fichier = "text.txt"

if os.path.exists(nom_fichier):
    print(f"Le fichier {nom_fichier} existe.")
else:
    print(f"Le fichier {nom_fichier} n'existe pas.")

print("---------------------------")

nom_fichier = "donnees.txt"

try:
    with open(nom_fichier, "r", encoding="utf-8") as f:
        contenu = f.read()
        print(contenu)
except FileNotFoundError:
    print("Fichier introuvable :", nom_fichier)


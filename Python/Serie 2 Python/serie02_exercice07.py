import json

# Données de l'exercice 3
commandes = [
    {"id": 1, "client": "alice@example.com", "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com", "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com", "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com", "montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com", "montant": 35.0, "statut": "payee"},
]

# PARTIE 1 : Afficher en JSON
print("PARTIE 1 : Affichage JSON")
json_str = json.dumps(commandes, indent=2, ensure_ascii=False)
print(json_str)

# PARTIE 2 : Sauvegarder dans un fichier
print("\nPARTIE 2 : Sauvegarde dans commandes.json")
with open("commandes.json", "w", encoding="utf-8") as f:
    json.dump(commandes, f, indent=2, ensure_ascii=False)
print("✓ Fichier créé !")

# PARTIE 3 : Lire et analyser
print("\nPARTIE 3 : Lecture et analyse")
with open("commandes.json", "r", encoding="utf-8") as f:
    commandes_lues = json.load(f)

print(f"Nombre de commandes lues : {len(commandes_lues)}")

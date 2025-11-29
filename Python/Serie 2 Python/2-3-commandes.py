commandes = [
    {"id": 1, "client": "alice@example.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",    "montant": 35.0,  "statut": "payee"},
]
#1. Afficher les commandes payées
sum = 0
for commande in commandes:
    if commande["statut"] == "payee":
        sum += commande["montant"]
print("Montant total des commandes payées :", sum)

#2. Compter le nombre de commandes par statut 
statuts = ["payee", "annulee", "en_attente"]
for statut in statuts:
    print(f"Commandes avec le statut {statut} :", len([commande for commande in commandes if commande["statut"] == statut]))

#3. Calculer le montant total dépensé par chaque client (tous statuts confondus) et le stocker dans un dictionnaire

clients = {}
for commande in commandes:
    if commande["statut"] not in clients:
        clients[commande["statut"]] = 0
    clients[commande["statut"]] += commande["montant"]
print("Montant total dépensé par client :", clients)
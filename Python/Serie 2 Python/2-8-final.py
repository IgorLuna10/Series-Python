import json

# Fonctions d'analyse (exercice 4)
def calculer_ca(commandes):
    """Calcule le chiffre d'affaires des commandes payées."""
    ca = 0
    for cmd in commandes:
        if cmd["statut"] == "payee":
            ca += cmd["montant"]
    return ca


def compter_commandes_par_statut(commandes):
    """Compte le nombre de commandes par statut."""
    compteurs = {}
    for cmd in commandes:
        statut = cmd["statut"]
        if statut in compteurs:
            compteurs[statut] += 1
        else:
            compteurs[statut] = 1
    return compteurs


def totaux_par_client(commandes):
    """Calcule le total dépensé par client."""
    totaux = {}
    for cmd in commandes:
        client = cmd["client"]
        montant = cmd["montant"]
        if client in totaux:
            totaux[client] += montant
        else:
            totaux[client] = montant
    return totaux


# Lecture du fichier JSON
with open("commandes.json", "r", encoding="utf-8") as f:
    commandes = json.load(f)

# Calcul des statistiques
ca = calculer_ca(commandes)
stats_statut = compter_commandes_par_statut(commandes)
totaux_clients = totaux_par_client(commandes)

# Tri des clients par montant décroissant (bonus)
clients_tries = sorted(totaux_clients.items(), key=lambda x: x[1], reverse=True)

# Affichage du tableau de bord
print("=== Tableau de bord commandes ===")
print()
print(f"Chiffre d'affaires (commandes payées) : {ca:.2f} €")
print()

print("Nombre de commandes par statut :")
for statut, nombre in stats_statut.items():
    print(f"  - {statut} : {nombre}")
print()

print("Top clients :")
for client, total in clients_tries:
    print(f"  - {client} : {total:.2f} €")
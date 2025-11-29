commandes = [
    {"id": 1, "client": "alice@example.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",    "montant": 35.0,  "statut": "payee"},
]
#1

def total_paid(commandes):
    total = 0
    for x in commandes:
        if x["statut"] == "payee":
            total += float(x["montant"])
    return total

#2

def count_status(commandes):
    status_counts = {}
    for x in commandes:
        statut = x["statut"]
        if statut not in status_counts:
            status_counts[statut] = 0
        status_counts[statut] += 1
    return status_counts

#3

def total_spent_by_client(commandes):
    total = {}
    for x in commandes:
        client = x["client"]
        montant = float(x["montant"])
        if client not in total:
            total[client] = 0
        total[client] += montant
    return total

if __name__ == "__main__":
    print(total_paid(commandes))
    print(count_status(commandes))
    print(total_spent_by_client(commandes))
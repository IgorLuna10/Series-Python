class Client:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email


class LigneCommande:
    def __init__(self, description, quantite, prix_unitaire):
        self.description = description
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire
    
    def total_ligne(self):
        return self.quantite * self.prix_unitaire
    
class Commande:
    def __init__ (self, client, lignes):
        self.client = client
        self.lignes = lignes

    def ajouter_ligne(self, ligne):
        self.lignes.append(ligne)

    def total(self):
        total = 0
        for ligne in self.lignes:
            total += ligne.total_ligne()
        return total
    
if __name__ == "__main__":
    print("=== Création de la commande ===\n")

    client1 = Client("Alice", "alice@example.com")
    ligne1 = LigneCommande("Lapin", 10, 10)
    ligne2 = LigneCommande("Cochon d'Inde", 5, 15)
    ligne3 = LigneCommande("Dragon", 2, 20)
    ligne4 = LigneCommande("Licorne", 1, 100)
    ligne5 = LigneCommande("Phénix", 3, 50)

    commande1 = Commande(client1, [ligne1, ligne2])

    print(f"Client: {commande1.client.nom}, Email: {commande1.client.email}")
    print("Lignes de commande initiales:")
    for ligne in commande1.lignes:
        print(f"Description: {ligne.description}, Quantité: {ligne.quantite}, Prix unitaire: {ligne.prix_unitaire}")
    print(f"Total initial de la commande: {commande1.total()}€\n")

donnees_produits = [
    {"id": 1, "nom": "Clavier",  "categorie": "Informatique", "prix": 39.99, "stock": 10},
    {"id": 2, "nom": "Souris",   "categorie": "Informatique", "prix": 19.99, "stock": 0},
    {"id": 3, "nom": "Écran",    "categorie": "Informatique", "prix": 129.90, "stock": 5},
    {"id": 4, "nom": "Chaise",   "categorie": "Bureau",       "prix": 89.90, "stock": 2}
]


class Produit:
    def __init__(self, id, nom, categorie, prix, stock):
        self.id = id
        self.nom = nom
        self.categorie = categorie
        self.prix = prix
        self.stock = stock

    def est_en_rupture(self):
        return self.stock == 0
    
    def afficher_resume(self):
        print(f"[{self.categorie}] {self.nom} - {self.prix}€ (stock : {self.stock})")

class Catalogue:
    def __init__(self):
        self.produits = []

    def ajouter_produit(self, produit):
        """Ajoute un objet Produit au catalogue"""
        self.produits.append(produit)

    def produits_par_categorie(self, categorie):
        """Retourne la liste des produits d'une catégorie donnée"""
        return [p for p in self.produits if p.categorie == categorie]

    def prix_moyen(self):
        """Calcule et retourne le prix moyen de tous les produits"""
        if not self.produits:
            return 0
        total = sum(p.prix for p in self.produits)
        return total / len(self.produits)

    def produits_en_rupture(self):
        """Retourne la liste des produits en rupture de stock"""
        return [p for p in self.produits if p.est_en_rupture()]


# Bloc principal
if __name__ == "__main__":
    # Créer le catalogue
    catalogue = Catalogue()
    
    # Convertir chaque dictionnaire en objet Produit et l'ajouter au catalogue
    for data in donnees_produits:
        produit = Produit(**data)
        catalogue.ajouter_produit(produit)
    
    # Afficher le prix moyen
    print(f"Prix moyen des produits : {catalogue.prix_moyen():.2f}€")
    print()
    
    # Afficher les produits en rupture
    print("Produits en rupture de stock :")
    ruptures = catalogue.produits_en_rupture()
    if ruptures:
        for produit in ruptures:
            produit.afficher_resume()
    else:
        print("Aucun produit en rupture")
    print()
    
    # Afficher les produits de la catégorie "Informatique"
    print("Produits de la catégorie 'Informatique' :")
    produits_info = catalogue.produits_par_categorie("Informatique")
    for produit in produits_info:
        produit.afficher_resume()
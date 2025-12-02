class Produit:
    def __init__(self, nom: str, prix_ht: float, stock: int):
        self.nom = nom
        self.prix_ht = prix_ht
        self.stock = stock
    
    def prix_ttc(self, taux_tva):
        return self.prix_ht * (1 + taux_tva)
    
    def valeur_stock_ttc(self, taux_tva):
        return self.stock * self.prix_ttc(taux_tva)
    
    def afficher(self):
        print(f"Produit: {self.nom}, prix HT : {self.prix_ht}€, prix TTC : {self.prix_ttc(0.2)}€, stock : {self.stock}, valeur du stock TTC : {self.valeur_stock_ttc(0.2)}€")

    def somme_stock_ttc(self, autres_produits, taux_tva):
        total = self.valeur_stock_ttc(taux_tva)
        for produit in autres_produits:
            total += produit.valeur_stock_ttc(taux_tva)
        return total


p1 = Produit("Lapin", 10, 100)
p2 = Produit("Cochon d'Inde", 15, 50)
p3 = Produit("Dragon", 20, 200)

catalogue = [p1, p2, p3]

for Produit in catalogue:
    Produit.afficher()

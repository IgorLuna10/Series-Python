class Rectangle:
    def __init__(self, largeur, hauteur):
            self.largeur = largeur
            self.hauteur = hauteur

    def surface(self):
        return self.largeur * self.hauteur
        
    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)

    def afficher(self):
        print(f"Rectangle: largeur={self.largeur}, hauteur={self.hauteur}, surface={self.surface()}, périmètre={self.perimetre()}")

r1 = Rectangle(4, 5)
r1.afficher()

r2 = Rectangle(10, 2)
r2.afficher()

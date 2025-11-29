class Employe:
    def __init__(self, nom, salaire):
        self.nom = nom
        self.salaire = salaire

    def calcul_salaire(self):
        return self.salaire * 1.2
    
    def afficher(self):
        print(f"Nom: {self.nom}, Salaire: {self.salaire}, Salaire brut: {self.calcul_salaire()}")

class Developer(Employe):
    def __init__(self, nom, salaire, prime_tech):
        super().__init__(nom, salaire)
        self.prime_tech = prime_tech
    def calcul_salaire(self):
        salaire_base = super().calcul_salaire()
        return salaire_base + self.prime_tech

class Manager(Employe):
    def __init__(self, nom, salaire, prime_gestion):
        super().__init__(nom, salaire)
        self.prime_gestion = prime_gestion

    def calcul_salaire(self):
        salaire_base = super().calcul_salaire()
        return salaire_base + self.prime_gestion
    
if __name__ == "__main__":
    print("=== Création des employés ===\n")

employe_alice = Developer("Alice", 5000, 122)
employe_bob = Developer("Bob", 4000, 100)
employe_charlie = Employe("Charlie", 3000)
employe_david = Manager("David", 4000, 500)

employes = [
    employe_alice,
    employe_bob,
    employe_charlie,
    employe_david
]

print("=== Affichage des employés ===\n")
for employé in employes:
    employé.afficher()
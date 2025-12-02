class CompteBancaire:
    
    def __init__(self, titulaire: str, solde: float = 0):
        self.titulaire = titulaire
        self.solde = solde
    
    def deposer(self, montant: float) -> None:
        """Ajoute de l'argent sur le compte."""
        if montant > 0:
            self.solde += montant
            print(f"Dépôt de {montant}€ effectué. Nouveau solde : {self.solde}€")
        else:
            print("Erreur : Le montant du dépôt doit être positif.")
    
    def retirer(self, montant: float) -> None:
        """Retire de l'argent du compte."""
        if montant <= 0:
            print(" Erreur : Le montant du retrait doit être positif.")
        elif montant > self.solde:
            print(f" Erreur : Fonds insuffisants. Vous avez {self.solde}€ mais vous voulez retirer {montant}€.")
        else:
            self.solde -= montant
            print(f"Retrait de {montant}€ effectué. Nouveau solde : {self.solde}€")
    
    def afficher(self) -> None:
        """Affiche les informations du compte."""
        print(f"\n--- Compte de {self.titulaire} ---")
        print(f"Solde actuel : {self.solde}€")
        print("---" + "-" * len(self.titulaire) + "---\n")


if __name__ == "__main__":
    print("=== Création du compte bancaire ===\n")
    
    compte_alice = CompteBancaire("Alice")
    compte_alice.afficher()
    
    print("=== Opérations bancaires ===\n")
    
    compte_alice.deposer(100)
    compte_alice.deposer(50)
    compte_alice.deposer(-20)
    compte_alice.retirer(30)
    compte_alice.retirer(200)
    compte_alice.retirer(50)
    
    print("\n=== Solde final ===")
    compte_alice.afficher()

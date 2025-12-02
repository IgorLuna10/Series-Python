class CommandeInvalideError (Exception):
    pass

def valider_commande(montant):
    if montant <= 0:
        raise CommandeInvalideError("Montant invalide. Veuillez entrer un montant positif.")
    
    if montant > 10000:
        raise CommandeInvalideError("Montant invalide. Veuillez entrer un montant inférieur à 10000.")
    
    return True

if __name__ == "__main__":
     
    try:
        x = int(input("Montant : "))
        valider_commande(x)
        print(f'{x} est un montant valide.')

    except ValueError:
        print("Erreur : Veuillez entrer un nombre entier valide.")
    

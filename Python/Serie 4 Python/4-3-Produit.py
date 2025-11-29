produits = ["PC Portable", "Écran", "Clavier", "Souris", "Casque"]

try:
    index = int(input("Indice : "))
    
    if index < 0:
        raise ValueError("Indice invalide. Veuillez entrer un nombre positif entre 0 et", len(produits)-1)
    else:
        print("Produit :", produits[index])
        
except ValueError:
    print("Indice invalide. Veuillez entrer un nombre entier.")
except IndexError:
    print("Indice invalide. Veuillez entrer un nombre entre 0 et", len(produits)-1)
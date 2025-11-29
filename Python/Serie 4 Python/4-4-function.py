def lire_fichier_securise(nom_fichier):

    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
        return contenu
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier}' est introuvable.")
        return None


# Bloc principal
if __name__ == "__main__":
    nom_fichier = input("Entrez le nom du fichier à lire : ")
    
    resultat = lire_fichier_securise(nom_fichier)
    
    if resultat is not None:
        print("\n--- Contenu du fichier ---")
        print(resultat)
    else:
        print("Lecture impossible.")
while True:
    try:
        age = int(input("Veuillez entrer votre âge : "))
        if age < 0:
            raise ValueError
        if age > 110:
            raise ValueError
        break  # Sort de la boucle si la conversion réussit

    except ValueError:
        print("Erreur : Veuillez saisir un nombre entier valide.")

print(f"Vous avez {age} ans.")
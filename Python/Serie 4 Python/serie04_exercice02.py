while True:
    try:
        x = int(input("Veuillez entrer un nombre : "))
        y = int(input("Veuillez entrer un nombre : "))

        result = x / y
    except ValueError:
        print("Erreur : Veuillez saisir un nombre valide.")
        continue
    except ZeroDivisionError:
        print("Erreur : Division par zéro impossible.")
        continue
    else:
        print(f"Le résultat de {x} divisé par {y} est {result}.")
        break

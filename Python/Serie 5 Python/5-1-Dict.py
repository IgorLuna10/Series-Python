def get_age_lbyl(utilisateur):
    #Approche LBYL (Look Before You Leap)
    if "age" in utilisateur:
        return utilisateur["age"]
    else:
        print("LBYL : La clé 'age' n'existe pas.")
        return None

def get_age_eafp(utilisateur):
    #Approche EAFP (Easier to Ask for Forgiveness than Permission)
    try:
        return utilisateur["age"]
    except KeyError:
        print("EAFP : La clé 'age' n'existe pas.")
        return None

if __name__ == "__main__":
    # Dictionnaire avec la clé "age"
    utilisateur_avec_age = {
        "nom": "Alice",
        "email": "alice@example.com",
        "age": 30
    }
    
    # Dictionnaire sans la clé "age"
    utilisateur_sans_age = {
        "nom": "Bob",
        "email": "bob@example.com"
    }
    
    print("=== Test avec un utilisateur qui a un âge ===")
    print(f"LBYL : {get_age_lbyl(utilisateur_avec_age)}")
    print(f"EAFP : {get_age_eafp(utilisateur_avec_age)}")
    
    print("\n=== Test avec un utilisateur sans âge ===")
    print(f"LBYL : {get_age_lbyl(utilisateur_sans_age)}")
    print(f"EAFP : {get_age_eafp(utilisateur_sans_age)}")
def appliquer_remise(prix: float, remise: float) -> float:
    """
    Calcule le prix final après une réduction.
    
    Par exemple : si un article coûte 100€ et qu'il y a 20% de remise,
    le prix final sera 80€.
    
    prix : le prix de départ (exemple : 100.0)
    remise : la remise en décimal (exemple : 0.2 pour 20%)
    
    Retourne : le prix après la remise
    
    Exemple :
    >>> appliquer_remise(100, 0.2)
    80.0
    """
    # On calcule : prix × (1 - remise)
    # Si prix = 100 et remise = 0.2, alors : 100 × (1 - 0.2) = 100 × 0.8 = 80
    prix_final = prix * (1 - remise)
    return prix_final


def compter_commandes_superieures(commandes: list[float], seuil: float) -> int:
    """
    Compte combien de commandes dépassent un certain montant.
    
    Par exemple : si on a des commandes de [50, 100, 150] et un seuil de 100,
    la fonction retourne 2 (car 100 et 150 sont >= 100).
    
    commandes : liste des montants (exemple : [50, 100, 150])
    seuil : le montant minimum à compter (exemple : 100)
    
    Retourne : le nombre de commandes qui dépassent le seuil
    
    Exemple :
    >>> compter_commandes_superieures([50, 100, 150, 75], 100)
    2
    """
    # On commence avec 0 commande comptée
    compteur = 0
    
    # On regarde chaque commande une par une
    for montant in commandes:
        # Si le montant est assez grand
        if montant >= seuil:
            # On ajoute 1 au compteur
            compteur += 1
    
    # On retourne le total
    return compteur


def normaliser_email(email: str) -> str:
    """
    Nettoie une adresse email : enlève les espaces et met tout en minuscules.
    
    Par exemple : "  Alice@EXAMPLE.com  " devient "alice@example.com"
    
    email : l'adresse email à nettoyer
    
    Retourne : l'email nettoyé
    
    Exemple :
    >>> normaliser_email("  Alice@EXAMPLE.com  ")
    'alice@example.com'
    """
    # .strip() enlève les espaces au début et à la fin
    # .lower() transforme tout en minuscules
    return email.strip().lower()


if __name__ == "__main__":
    # === TEST 1 : Appliquer une remise ===
    print("=== Test 1 : Remise ===")
    prix_original = 100
    taux_remise = 0.2  # 20% de remise
    prix_apres_remise = appliquer_remise(prix_original, taux_remise)
    print(f"Prix original : {prix_original}€")
    print(f"Remise : {taux_remise * 100}%")
    print(f"Prix final : {prix_apres_remise}€")
    
    # === TEST 2 : Compter les commandes ===
    print("\n=== Test 2 : Compter les commandes ===")
    mes_commandes = [45.50, 120.00, 89.99, 150.00, 75.00]
    montant_minimum = 100
    nombre = compter_commandes_superieures(mes_commandes, montant_minimum)
    print(f"Liste des commandes : {mes_commandes}")
    print(f"Combien de commandes >= {montant_minimum}€ ? Réponse : {nombre}")
    
    # === TEST 3 : Nettoyer un email ===
    print("\n=== Test 3 : Nettoyer un email ===")
    email_sale = "  Alice@EXAMPLE.com  "
    email_propre = normaliser_email(email_sale)
    print(f"Email avant : '{email_sale}'")
    print(f"Email après : '{email_propre}'")
    
    # === BONUS : Afficher l'aide ===
    print("\n=== Aide sur la fonction appliquer_remise ===")
    help(appliquer_remise)

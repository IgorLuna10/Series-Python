def est_pair(n):
    if n % 2 == 0:
        return True
    else:
        return False

def calculer_tva(prix_ht, taux):
    """Retourne le prix TTC en appliquant la TVA"""
    tva = prix_ht * taux / 100
    return prix_ht + tva

def moyenne(liste_nombres):
    if len(liste_nombres) == 0:
        return 0  
    total = sum(liste_nombres)
    return total / len(liste_nombres)
    
if __name__ == "__main__":

    print(est_pair(10))
    print(est_pair(11))
    print(calculer_tva(100, 20))
    print(moyenne([15, 22, 43, 64, 85]))

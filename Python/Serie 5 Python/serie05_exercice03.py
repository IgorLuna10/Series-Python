def calculer_moyenne(notes: list[float]) -> float:
    return sum(notes) / len(notes)

def filtrer_notes_suffisantes(notes: list[float], seuil: float) -> list[float]:
    result = []
    for n in notes:
        if n >= seuil:
            result.append(n)
    return result

def formater_message(nom: str, moyenne: float) -> str:
    return f"Étudiant {nom} : moyenne = {moyenne:.2f}"

if __name__ == "__main__":
    # Créer une liste de notes
    notes_etudiant: list[float] = [8.5, 12.0, 15.5, 9.0, 14.0, 11.5, 7.0]
    
    # Calculer la moyenne
    moyenne: float = calculer_moyenne(notes_etudiant)
    
    # Filtrer les notes >= 10
    notes_suffisantes: list[float] = filtrer_notes_suffisantes(notes_etudiant, 10.0)
    
    # Afficher un message formaté
    nom_etudiant: str = "Alice"
    message: str = formater_message(nom_etudiant, moyenne)
    
    print(message)
    print(f"Notes suffisantes (>= 10) : {notes_suffisantes}")
    print(f"Nombre de notes suffisantes : {len(notes_suffisantes)}/{len(notes_etudiant)}")

#1.

notes = []
with open("notes.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.strip()  # enlève les espaces et retours à la ligne
        if ligne:  # vérifie que la ligne n'est pas vide
            notes.append(float(ligne))

print(notes)

#2.

if notes:  # vérifie que la liste n'est pas vide
    # Min et Max
    note_min = min(notes)
    note_max = max(notes)
    
    # Moyenne
    moyenne = sum(notes) / len(notes)
    
    # Nombre de notes >= 10
    nb_notes_reussies = 0
    for note in notes:
        if note >= 10:
            nb_notes_reussies += 1
    
    # Affichage des résultats
    print(f"Note minimale : {note_min}")
    print(f"Note maximale : {note_max}")
    print(f"Moyenne : {moyenne:.2f}")
    print(f"Nombre de notes >= 10 : {nb_notes_reussies}")
else:
    print("Aucune note trouvée dans le fichier")
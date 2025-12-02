notes = [12, 5.5, 17, 9, 13, 8, 10]

print("Min:", min(notes))
print("Max:", max(notes))
print(f"Average: {sum(notes) / len(notes):.2f}")

compteur = 0

for note in notes:
    if note >= 10:
        compteur += 1
print("Number of passing grades:", compteur)

percentage = compteur / len(notes) * 100
print(f"Percentage of passing grades: {percentage:.2f}%")

list_prix_float = [1.5, 2.5, 3.5, 4.5, 5.5]

total = 0

for i in range(len(list_prix_float)):
  print(list_prix_float[i], end=" ")
print()

total = sum(list_prix_float)
print(total)

# Calculate average
average = total / len(list_prix_float)
print(average)
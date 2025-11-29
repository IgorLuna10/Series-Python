
n = int(input("Entrez un nombre : "))

for i in range(1, 11):
  print(n, "x", i, "=", n * i)

somme = 0
i = 1

while i <= 10:
  somme = somme + i
  i = i + 1

print("La somme de 1 a 10 est : ", somme)
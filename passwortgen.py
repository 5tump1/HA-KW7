# Generiere ein zufälliges Passwort mit 10 Stellen aus Großbuchstaben
import random
passwort = ""

chr(65)

liste = []
i = 65  # ASCII Tabelle A
while i <= 90:  # bis 90 ASCII Tabelle Z
    liste.append(chr(i))
    i+=1

#print(liste)

for j in range(10):
    add = random.choice(liste)
    passwort += add
print(passwort)

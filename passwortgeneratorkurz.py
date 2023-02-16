# Simpler Passwortgenerator
# 33 - 126, Kleinbuchstaben, Großbuchstaben, Zahlen, Alle Sonderzeichen aus ASCII

from random import randint

passwort = ""

for i in range(12):
    add = chr(randint(33, 126))
    passwort += add
print(passwort)

from random import randint
import re

passwort = ""

for i in range(12):
    add = chr(randint(33, 126))
    passwort += add
#print(passwort)

numpattern = r'(\d)'
ucpattern = r'[A-Z]' # Prüfen was genau \p{Lu}
lcpattern = r'[a-z]'
sppattern = r'(\W)'


def numcheck(wort): # Single Responsibility: Eine Aufgabe, finde Zahl
    if re.search(numpattern, wort):
        return True
    else:
        return False

def uppercasecheck(wort):
    if re.search(ucpattern, wort):
        return True
    else:
        return False

def lowercasecheck(wort):
    if re.search(lcpattern, wort):
        return True
    else:
        return False

def specialcheck(wort):
    if re.search(sppattern, wort):
        return True
    else:
        return False

def laengecheck(wort):
    if 8 <= len(wort) <= 16:
        return True
    else:
        return False

def repitioncheck(wort):
    for i in range(0, len(wort) - 2):
        if wort[i] == wort[i + 1] == wort[i + 2]:
            return False
        else:
            return True

def passwortpruefer(wort):
    if numcheck(wort) and uppercasecheck(wort) and lowercasecheck(wort) and specialcheck(wort) and laengecheck(wort):
        print("Gültig")
    else:
        print("Ungültig")

def genpassword(length = 12):
    passwort = ""
    for i in range(12):
        add = chr(randint(33, 126))
        passwort += add

while True:
    if passwortpruefer(passwort) == "Ungueltig":
        passwort = genpassword()
    else: 
        break

print(passwort)
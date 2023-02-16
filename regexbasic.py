import re

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

def passwortpruefer(wort):
    if numcheck(wort) and uppercasecheck(wort) and lowercasecheck(wort) and specialcheck(wort) and laengecheck(wort):
        print("Gültig")
    else:
        print("Ungültig")


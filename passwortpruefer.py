# Prüfen ob PW valide: Min.: 1 Großbuchstaben, 1 Kleinbuchstaben, eine Ziffer, ein Sonderzeichen
# Passwortlänge mindestens 8 und maximal 16

# ==
# booleans True / False

def istvalide(password):
    if 8 <= len(password) <= 16:
        lc = False
        uc = False
        num = False
        special = False

        for char in password:
            if char.isdigit():
                num = True
            if char.islower():
                lc = True
            if char.isupper():
                uc = True
            if not char.isalnum():
                special = True
        return lc and uc and num and special
    else:
        return False


passworteingabe = input("Zu testendes Passwort eingeben: ")
print(istvalide(passworteingabe))

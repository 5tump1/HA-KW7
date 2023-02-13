# Calculator
#Titel ausgeben
print("Taschenrechner\n")
#Funktionen
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b
#funktion ob integer oder float (kommazahl muss mit punkt geschrieben werden)
def int_or_float(zahl):
    if "." in zahl:
        return float(zahl)
    else:
        return int(zahl)
#Benutzereingabe
while True:
    #erste zahl eingeben
    zahl1 = int_or_float(input("erste Zahl: "))
    #zweite zahl eingeben
    zahl2 = int_or_float(input("zweite Zahl: "))
    #welche rechenoperation soll durchgeführt werden
    operator = input("Addieren (+), Subtrahieren (-), Multiplizieren (*), Dividieren (/) : " )
    #ergebnis auf null setzen
    ergebnis = 0
    #Bedingungen/Funktionen
    if operator == "+":
        ergebnis = add(zahl1, zahl2)
    elif operator == "-":
        ergebnis = sub(zahl1, zahl2)
    elif operator == "*":
        ergebnis = mult(zahl1, zahl2)
    elif operator == "/":
        ergebnis = div(zahl1, zahl2)
    #Ergebnis anzeigen:
    print(f"{zahl1} {operator} {zahl2} = ", (ergebnis))


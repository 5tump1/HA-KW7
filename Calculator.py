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
#Benutzereingabe
#erste zahl eingeben
zahl1 = float(input("erste Zahl: "))
#zweite zahl eingeben
zahl2 = float(input("zweite Zahl: "))
#welche rechenoperation soll durchgeführt werden
operator = input("Addieren (+), Subtrahieren (-), Multiplizieren (*), Dividieren (/) : " )
#ergebnis auf null setzen
ergebnis = 0
#Bedingungen eingebaut
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
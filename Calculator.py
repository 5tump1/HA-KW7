# Calculator

#Benutzereingabe
#erste zahl eingeben
zahl1 = int(input("erste Zahl: "))
#zweite zahl eingeben
zahl2 = int(input("zweite Zahl: "))
#welche rechenoperation soll durchgeführt werden
operator = input("Addieren (+), Subtrahieren (-), Multiplizieren (*), Dividieren (/) : " )
#ergebnis auf null setzen
ergebnis = 0
#Bedingungen eingebaut
if operator == "+":
    ergebnis = zahl1+zahl2
if operator == "-":
    ergebnis = zahl1-zahl2
if operator == "*":
    ergebnis = zahl1*zahl2
if operator == "/":
    ergebnis = zahl1/zahl2

#Ergebnis anzeigen:
print(f"{zahl1} {operator} {zahl2} = ", (ergebnis))

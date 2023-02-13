# Calculator

#Benutzereingabe
zahl1 = int(input("erste Zahl: "))
zahl2 = int(input("zweite Zahl: "))
operator = input("Addieren (+), Subtrahieren (-), Multiplizieren (*), Dividieren (/) : " )

ergebnis=0

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

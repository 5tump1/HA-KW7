#Aufgabe Bank --erweiterte hausaufagbe--

class bankkonto:
    def __init__(self, besitzer, kontostand):
        self.besitzer = besitzer
        self.kontostand = kontostand
    def __str__(self):
        return f"Dieses Konto gehört {self.besitzer} und hat ein Guthaben von {self.kontostand}"
    def abfrage_kontostand(self):
        print(f"der kontostand beträgt {self.kontostand}")
    def abfrage_besitzer(self):
        print(f"der besitzer des kontos ist {self.besitzer}")

    def einzahlen(self, betrag):
        self.kontostand += betrag
    
    def auszahlen(self, betrag):
        if betrag > self.kontostand:
            print("Sorry, aber du hast nicht genug geld!")
        else:
            self.kontostand = self.kontostand - betrag
class kindersparkonto(bankkonto):
    def __init__(self, besitzer, kind, kontostand):
        super().__init__(besitzer, kontostand)
        self.kind = kind

konten = {
    "chris": bankkonto("Christopher", 250.00),
    "padde" : bankkonto("Patrick", 300.00),
    "uli" : bankkonto("Uli", 145.00),
}

print(konten["chris"])
print(konten["padde"])
print(konten["uli"])

str_konto = input("Welches Konto möchten Sie bearbeiten [Chris, Padde, Uli]? ").lower()
str_aktion = input("Möchten sie ein- oder auszahlen [Einzahlen, Auszahlen]? ").lower()

str_betrag = input(f"Welchen betrag möchten sie {str_aktion}? ")

if str_aktion.lower() == "einzahlen":
    konten[str_konto].einzahlen(float(str_betrag))
elif str_aktion == "auszahlen":
    konten[str_konto].auszahlen(float(str_betrag))
else:
    print("Konnte Aktion \"{str_aktion}\" nicht verstehen")
print(f"Neuer Kontostand von {konten[str_konto].besitzer} beträgt "
      f"{konten[str_konto].kontostand}")

""""
class kredit:
    def __init__(self, kreditvolumen):
        super().__init__(besitzer, kreditvolumen)
        self.kreditvolumen = kreditvolumen

kreditvolumen = {
    "chris" : kredit("Christopher", 10000.0),
    "padde" : kredit("Patrick", 150000.45),
    "uli" : kredit("Uli", 12000.33),
}

print(kredit["chris"])
print(kredit["padde"])
print(kredit["uli"])
"""
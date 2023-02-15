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

konten = {
    "chris": bankkonto("Christopher", 250.00),
    "padde" : bankkonto("Patrick", 300.00),
    "uli" : bankkonto("Uli", 145.00),
}

print(konten["chris"])
print(konten["padde"])
print(konten["uli"])

class kinderkonto:
    def __init__(self, besitzer, kind, kontostand):
        super().__init__(besitzer, kontostand)
        self.kind = kind

class kredit:
    def __init__(self, besitzer, volumen):
        super().__init__(besitzer)
        self.volumen = kreditvolumen

volumen = {
    "chris" : kredit("Christopher", 10000.00),
    "padde" : kredit("Patrick", 150000.45),
    "uli" : kredit("Uli", 12000.33),
}

print(kredit["chris"])
print(kredit["padde"])
print(kreidt["uli"])

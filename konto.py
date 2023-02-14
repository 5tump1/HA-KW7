class bankkonto:
    def __init__(self, besitzer, kontostand):
        self.besitzer = besitzer
        self.kontostand = kontostand
    def __str__(self):
        return f"Dieses Bankkonto gehört {self.besitzer} und hat ein guthaben von {self.kontostand}"
    def abfrage_kontostand(self):
        print(f"Der Kontostand beträgt {self.kontostand}")
    def abfrage_besitzer(self):
        print(f"Der Besitzer des kontos ist {self.besitzer}")

    def einzahlen(self, betrag):

    def auszahlen(self, betrag):


chris = bankkonto("Chris", 100.00)
padde = bankkonto("Padde", 245.89)

print(chris)
print(padde)





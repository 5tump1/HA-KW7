class bankkonto:
    def __init__(self, besitzer, kontostand):
        self.besitzer = besitzer
        self.kontostand = kontostand
    def abfrage_kontostand(self):
        print(f"Der Kontostand beträgt {self.kontostand}")
    def abfrage_besitzer(self):
        print(f"Der Besitzer des kontos ist {self.besitzer}")


chris = bankkonto("Chris", 100.00)
padde = bankkonto("Padde", 245.89)

print(f"{chris.besitzer}: {chris.kontostand}")
print(f"{padde.besitzer}: {padde.kontostand}")
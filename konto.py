class bankkonto:
    def __init__(self, besitzer, kontostand):
        self.besitzer = besitzer
        self.kontostand = kontostand
    def __str__(self):
        return f"Dieses Bankkonto gehört {self.besitzer} und hat ein Guthaben von {self.kontostand}"
    def abfrage_kontostand(self):
        print(f"Der Kontostand beträgt {self.kontostand}")
    def abfrage_besitzer(self):
        print(f"Der Besitzer des Kontos ist {self.besitzer}")

    def einzahlen(self, betrag):
        self.kontostand = self.kontostand + betrag
        #self.kontostand += betrag
    def auszahlen(self, betrag):
        if betrag > self.kontostand:
            print("Sorry: du kannst nicht mehr geld abheben als du hast!")
        else:
            self.kontostand = self.kontostand - betrag

konten = {
    "uli": bankkonto("Sir U. v. Liechtenstein", 100.0),
    "simo": bankkonto("Simo", 2_500_000),
    "chris": bankkonto("Christopher Stumpe", 2_500),
    }

print(konten["simo"])
print(konten["uli"])
print(konten["chris"])

str_konto = input("Welches Konto möchten Sie bearbeiten [Simo, Uli]? ").lower()
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

class bankkonto:
    def __init__(self, eigentuemer, kontostand):
        self.eigentuemer = eigentuemer
        self.kontostand = kontostand


chris = bankkonto("Chris", 100.00)
padde = bankkonto("Padde", 245.89)

print(f"{chris.eigentuemer}: {chris.kontostand}")
print(f"{padde.eigentuemer}: {padde.kontostand}")
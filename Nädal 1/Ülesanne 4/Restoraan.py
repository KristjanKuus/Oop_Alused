class Restoraan():
    restoraani_nimi = ""
    soogi_tyyp = ""

    def kirjelda_restoraan(self):
        print("Restoraan " + str(self.restoraani_nimi) + ", söögi tüüp " + str(self.soogi_tyyp))

    def ava_restoraan(self):
        print("Restoraan", str(self.restoraani_nimi)  , "on avatud!")
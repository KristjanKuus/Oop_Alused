class Restoraan():
    def __init__(self, restoraani_nimi, soogi_tyyp, teenindatud_kylastajad):
        self.restoraani_nimi = restoraani_nimi
        self.soogi_tyyp = soogi_tyyp
        self.teenindatud_kylastajad = teenindatud_kylastajad

    def kirjelda_restoraan(self):
        print("Restoraan " + str(self.restoraani_nimi) + ", söögi tüüp " + str(self.soogi_tyyp))

    def ava_restoraan(self):
        print("Restoraan", str(self.restoraani_nimi)  , "on avatud!")

    def määra_teenindatud_kylalised(self, x):
        print("Varem oli teenindatud külaliste arv", self.teenindatud_kylastajad)
        self.teenindatud_kylastajad = x
        print("teenindatud külaliste arv on määratud, arv on nüüd", x)

    def suurenda_teenindatud_kylalised(self, x):
        print("Teenindatud külaliste arv oli ennem", self.teenindatud_kylastajad)
        self.teenindatud_kylastajad = self.teenindatud_kylastajad + x
        print("Teenindatud külaliste arv on nüüd", self.teenindatud_kylastajad)
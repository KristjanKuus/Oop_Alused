miinilist = []
class Inimene():
    def __init__(self, eesnimi, perenimi, kutsekvalifikatsioon):
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.kutsekvalifikatsioon = kutsekvalifikatsioon

    def __del__(self):
        miini = self.kutsekvalifikatsioon
        miinilist.append(miini)
        print(miinilist)
        if min(miinilist) > 0:
            print("Kõike head,", str(self.eesnimi) + ",", self.perenimi)
            del self
        else:
            print("Jätkage!")

    def tutvustus(self):
        print("Tere, olen", str(self.eesnimi), str(self.perenimi))


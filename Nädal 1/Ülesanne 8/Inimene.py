miinilist = []
class Inimene():
    def __init__(self, eesnimi, perenimi, kutsekvalifikatsioon):
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.kutsekvalifikatsioon = kutsekvalifikatsioon
        miini = self.kutsekvalifikatsioon
        miinilist.append(miini)

    def __del__(self):
        if self.kutsekvalifikatsioon == min(miinilist):
            print("Kõike head,", str(self.eesnimi) + ",", self.perenimi)
            del self
        else:
            pass

    def tutvustus(self):
        print("Tere, olen", str(self.eesnimi), str(self.perenimi))
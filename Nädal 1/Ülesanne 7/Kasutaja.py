class Kasutaja():
    def __init__(self, eesnimi, perenimi, privileeg = ""):
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.privileeg = privileeg

    def get_privileeg(self):
        return self.privileeg

    def set_privileeg(self, x):
        self.privileeg = x

    def kirjelda_kasutaja(self):
        print("nimi: "+ str(self.eesnimi) + " " + str(self.perenimi) + " privileegid on: "+ str(self.get_privileeg()))

    def tervita_kasutaja(self):
        print("Tere! " + str(self.eesnimi) + " " + str(self.perenimi))
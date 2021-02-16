class Kasutaja():
    def __init__(self, eesnimi, perenimi, sisselogimiskatsed, privileeg = "",):
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.privileeg = privileeg
        self.sisselogimiskatsed = sisselogimiskatsed

    def get_privileeg(self):
        return self.privileeg

    def set_privileeg(self, x):
        self.privileeg = x

    def kirjelda_kasutaja(self):
        print("nimi: "+ str(self.eesnimi) + " " + str(self.perenimi) + " privileegid on: "+ str(self.get_privileeg()))

    def tervita_kasutaja(self):
        print("Tere! " + str(self.eesnimi) + " " + str(self.perenimi))

    def suurenda_sisselogimiskatsed(self):
        self.sisselogimiskatsed = self.sisselogimiskatsed + 1
        print("Kasutajal on", self.sisselogimiskatsed, "sisselogimis katset")

    def reset_sisselogimiskatsed(self):
        self.sisselogimiskatsed = 0
        print("Kasutaja sisselogimis katsed on nullistatud")
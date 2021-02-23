class Kasutaja():
    def __init__(self, eesnimi, perenimi, privileeg, parool = "qwerty"):
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.privileeg = privileeg
        self.parool = parool

    def maara_parool(self, x):
        self.parool = x

    def naita_parool(self):
        print(self.parool)

    def kontrolli_parool(self, x):
        if len(x) >= 6 and len(x) < 11:
            print("Parooli vahetamine on õnnestunud")
            self.maara_parool(x)
        else:
            print("Parooli vahetamine ei õnnestunud", "\n", "Põhjus: Parool on liiga pikk")

    def kirjelda_kasutaja(self):
        print("Kasutaja:", self.eesnimi + self.perenimi, "Parool:", self.parool)

    def tervita_kasutaja(self):
        print("Tere! " + str(self.eesnimi) + " " + str(self.perenimi))
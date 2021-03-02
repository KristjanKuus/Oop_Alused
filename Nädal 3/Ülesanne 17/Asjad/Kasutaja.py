class Kasutaja():
    def __init__(self, eesnimi, perenimi, privileeg):
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.privileeg = privileeg


    def kirjelda_kasutaja(self):
        print("Kasutaja nimi: "+ str(self.eesnimi) + " " + str(self.perenimi) + " privileegid on: "+ str(self.privileeg) )

    def tervita_kasutaja(self):
        print("Tere! " + str(self.eesnimi) + " " + str(self.perenimi))

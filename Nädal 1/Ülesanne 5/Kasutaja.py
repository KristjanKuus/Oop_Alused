class Kasutaja():
    eesnimi = ""
    perenimi = ""
    privileeg = ""

    def kirjelda_kasutaja(self):
        print("Kasutaja nimi: "+ str(self.eesnimi) + " " + str(self.perenimi) + " privileegid on: "+ str(self.privileeg) )

    def tervita_kasutaja(self):
        print("Tere! " + str(self.eesnimi) + " " + str(self.perenimi))
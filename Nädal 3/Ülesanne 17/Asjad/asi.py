class Kasutaja():
    def __init__(self, eesnimi, perenimi, privileeg):
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.privileeg = privileeg


    def kirjelda_kasutaja(self):
        print("Kasutaja nimi: "+ str(self.eesnimi) + " " + str(self.perenimi) + " privileegid on: "+ str(self.privileeg) )

    def tervita_kasutaja(self):
        print("Tere! " + str(self.eesnimi) + " " + str(self.perenimi))

class Privileegid():
    def __init__(self, privileegid = "lubatud lisada kasutajad, lubatud eemaldada kasutajad, lubatud blokeerida kasutajad"):
        self.privileegid = privileegid

    def naita_privileegid(self):
        print(self.privileegid)


class Admin(Kasutaja, Privileegid):
    privileegid="lubatud lisada kasutajad, lubatud eemaldada kasutajad, lubatud blokeerida kasutajad"

    def privileegid_(self, privileegid):
        self.privileegid = privileegid


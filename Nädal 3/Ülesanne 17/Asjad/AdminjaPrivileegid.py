from Kasutaja import *
class Privileegid():
    def __init__(self, privileegid = "lubatud lisada kasutajad, lubatud eemaldada kasutajad, lubatud blokeerida kasutajad"):
        self.privileegid = privileegid

    def naita_privileegid(self):
        print(self.privileegid)


class Admin(Kasutaja, Privileegid):
    privileegid="lubatud lisada kasutajad, lubatud eemaldada kasutajad, lubatud blokeerida kasutajad"

    def privileegid_(self, privileegid):
        self.privileegid = privileegid


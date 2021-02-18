from random import randint
idlugeja = 0
armee1 = []
armee2 = []

class inimene:
    def __init__(self):
        self.id = 0

    def id_jagaja(self):
        global idlugeja
        while idlugeja == 0:
           if self.id == 0:
            self.id = 1
            idlugeja = idlugeja + 1
        while idlugeja >= 1:
            idlugeja = idlugeja + 1
            self.id = idlugeja - 1
            break

    def info(self):
        print("Inimse ID on:", self.id)

class sodur(inimene):
    def armee(self):
        self.armee = randint(1,2)

    def printer(self):
        print(self.id)

    def armeeleidja(self):
        if self.armee == 1:
            armee1.append(self.id)
        if self.armee == 2:
            armee2.append(self.id)

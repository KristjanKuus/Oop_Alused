from random import randint
class Sõdur():
    tervis = 100

def voitlus(sodur1, sodur2):
    while sodur2.tervis > 0 and sodur1.tervis > 0:
        kesloob = randint(1,2)
        if kesloob == 1:
            sodur2.tervis = sodur2.tervis - 20
            print("Esimene sõdur lõi!")
            print("Teisel sõduril on", (sodur2.tervis), "tervist!")
        else:
            sodur1.tervis = sodur1.tervis - 20
            print("Teine sõdur lõi!")
            print("Esimesel sõduril on", (sodur1.tervis), "tervist!")
        if sodur2.tervis == 0:
            print("Esimene sõdur võitis!")
        elif sodur1.tervis == 0:
            print("Teine sõdur võitis!")
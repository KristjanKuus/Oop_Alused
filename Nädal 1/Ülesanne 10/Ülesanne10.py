from Kasutaja import *

Kasutaja1 = Kasutaja("Jass", "Juss", 0)
Kasutaja2 = Kasutaja("Tege", "Lane", 0)
Kasutaja3 = Kasutaja("Jooma", "Mees", 0)

Kasutaja1.set_privileeg("Kasutaja")
Kasutaja2.set_privileeg("Kasutaja")
Kasutaja3.set_privileeg("Administraator")


Kasutaja1.kirjelda_kasutaja()
Kasutaja2.kirjelda_kasutaja()
Kasutaja3.kirjelda_kasutaja()

Kasutaja3.suurenda_sisselogimiskatsed()
Kasutaja3.suurenda_sisselogimiskatsed()
Kasutaja3.suurenda_sisselogimiskatsed()

Kasutaja3.reset_sisselogimiskatsed()
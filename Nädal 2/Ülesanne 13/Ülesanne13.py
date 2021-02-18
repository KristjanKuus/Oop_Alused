from Kasutaja import *

Kasutaja1 = Kasutaja("Jass", "Juss", "Kasutaja")
Kasutaja2 = Kasutaja("Tege", "Lane","Kasutaja")
Kasutaja3 = Kasutaja("Jooma", "Mees","Kasutaja")

Admin1 = Admin("Teet", "Peet", "Administraator")

Admin1.kirjelda_kasutaja()
Admin1.privileegid_("lubatud lisada kasutajad, lubatud eemaldada kasutajad, lubatud blokeerida kasutajad")
Admin1.naita_privileegid()
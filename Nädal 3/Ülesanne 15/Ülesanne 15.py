from Kasutaja import *

Kasutaja1 = Kasutaja("Jass", "Juss", "Kasutaja")
Kasutaja2 = Kasutaja("Tege", "Lane", "Kasutaja")
Kasutaja3 = Kasutaja("Jooma", "Mees", "Admin")

Kasutaja1.kontrolli_parool("vägalahe")
Kasutaja2.kontrolli_parool("LaneTege")
Kasutaja3.kontrolli_parool("KasTeginÕigesti")

Kasutaja1.kirjelda_kasutaja()
Kasutaja2.kirjelda_kasutaja()
Kasutaja3.kirjelda_kasutaja()
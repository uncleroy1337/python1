"""
1. Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!
"""

import random
veletlen_szam = random.randint(1, 3)
#print(veletlen_szam)
bekert = int(input("Kérem a számot!"))
if veletlen_szam == bekert:
    print("Megegyezik!")
else:
  print("Nem egyezik!")
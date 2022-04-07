'''
Nagyobb szám.
A program kérjen be két számot a felhasználótól, majd írja ki, hogy melyik a nagyobb! 
A program üzeneteinek megfogalmazásában kövesse az alábbi mintát:
--------------
Adj meg egy számot! 1
Adj meg egy másik számot! 17
A nagyobb érték 17
--------------
Adj meg egy számot! 28
Adj meg egy másik számot! -2
A nagyobb érték: 28
---------------
Adj meg egy számot! 999
Adj meg egy másik számot! 999
A két szám egyenlő
------------------
'''

elso_szam = int(input("Adj meg egy számot! "))
masodik_szam = int(input("Adj meg egy másik számot! "))

while True:
  if elso_szam > masodik_szam:
    print(f"A nagyobb érték: {elso_szam}")
    break
  elif elso_szam < masodik_szam:
    print(f"A nagyobb érték: {masodik_szam}")
    break
  elif elso_szam == masodik_szam:
    print("A két szám egyenlő.")
    break

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

elso_szam = int(input("Kérem az első számot!"))
masodik_szam = int(input("Kérem a második számot!"))

while True:
  if elso_szam > masodik_szam:
    print("Nagyobb a ", elso_szam, ","" mint a(z) ", masodik_szam)
    break
  elif elso_szam < masodik_szam:
    print("Nagyobb a ", masodik_szam, ",", "mint a(z)", elso_szam)
    break
  elif elso_szam == masodik_szam:
    print("A két szám egyenlő")
    break
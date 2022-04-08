'''
Készíts egy programot, amely a felhasználó által megadott mondatról a mondatvégi jel alapján eldönti milyen fajtájú! 
(kijelentő, kérdő, felkiáltó/felszólító)

'''

#megoldas

mondat = input("Írj ide egy mondatot:")
mjel = mondat[-1]

if mjel == "!":
  print("A mondat fajtája: Felkiáltó/Felszólító ")
elif mjel == "?":
  print("A mondat fajtája: Kérdő")
else:
  mjel == "."
  print("A mondat fajtája: Kijelentő")

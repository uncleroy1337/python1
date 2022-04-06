 ## Írjon programot jelszo.py néven, amely azt vizsgálja, hogy egy felhasználó helyesen adja-e meg a jelszavát! 
 ##A program addig kérdezi újra a felhasználónév-jelszó párost, amíg a felhasználó mindkettőt hibátlanul meg nem adja. 
 ##A program egyetlen felhasználó (sis) jelszavát (1234) ismeri, csak ezt a párost fogadja el helyesként. 
 ##Mind a sikertelen, mind a sikeres bejelentkezési kísérletekről üzenetet ír a képernyőre.

felhasznalonev = input('Kérem a felhasználó nevét: ')
password = input('Kérem a jelszót: ')
if felhasznalonev == "sis" and password == "1234":
  print("Üdvözlöm!")
else:
  print('Sikertelen bejelentkezés')

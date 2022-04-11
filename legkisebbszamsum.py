#. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
#  legkisebb értéket ezek közül!
#  Majd kiírja a három szám összegét




szamok = []
for i in range(3):
    szam = int(input("Adj meg három számot:"))
    szamok.append(szam)
szamok.sort()
print("A legkissebb megadott szám: ", szamok[:1])
print("A három szám összege: ", sum(szamok))

#feladat: A felhasználátol kérjen be egy számot a program és irja ki az addigi számok összegét.

#megoldás:
szam = int(input("kérek egy számot: "))
szamlalo = 0
for i in range(szam + 1):
    szamlalo = szamlalo + i
print(szamlalo)    
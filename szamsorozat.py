#feladat: A felhasználátol kérjen be egy számot, és az ebből készített számsorozatot adja össze, majd 

#példa
'''
kérek egy számot: 10
55
'''

#megoldás:
szam = int(input("kérek egy számot: "))
szamlalo = 0
for i in range(szam + 1):
    szamlalo += i #vagy szamlalo = szamlalo + i 
print(szamlalo)    

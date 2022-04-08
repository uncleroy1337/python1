"""
Írj egy programot, amely [1;12] intervallumon állít elő 30 darab véletlenszámot! 
A képernyőre kizárólag csak az 5-el oszthatóakat írja ki, majd jelenítse meg az összes véletlen
generált számot és a végén informálja a felhasználót arról is, hány darab ilyen szám volt.
"""
from random import randint

szamlista = [randint(1, 12)for szam in range(30)]
otteloszthato = len([szam for szam in szamlista if szam %5 == 0])
print(szamlista)
print(f'Öttel osztható számok száma: {otteloszthato}')

################################################################
#masik modszer

lista  = []
osszeg = []
for i in range(30):
    y = randint(1, 12)
    if y % 5 == 0:
        osszeg.append(y)        
    lista.append(y)
print(lista)
print(f'Öttel osztható számok száma: {len(osszeg)}')

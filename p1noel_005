#1. feladat: Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot és ezeket tárolja el egy listában!
A program számolja össze, és képernyőre írja ki a listában tárolt páros számok számát, valamint a lista elemeit!

import random
lista = []
paros = []

for i in range(5):
  a = random.randint(1, 10)
  lista.append(a)

for szam in lista:
  if szam % 2 == 0:
    paros.append(szam)

print(f"Páros számok száma: {len(paros)}")
print(f"A lista elemei: {lista}")

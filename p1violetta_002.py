''' 
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot 
és ezeket tárolja el egy listában! A program számolja össze és írja ki a képernyőre a 
listában tárolt páros számok számát, valamint a lista elemeit! 

'''

#megoldás

import random

lista = [random.randint(1,10) for i in range(5)]

paroslista = [i for i in lista if i % 2 == 0]

print(lista)
print(f"A páros számok száma:{len(paroslista)}")
print(paroslista)

''' Írjon egy programot ami kiírja a kettővel osztható számokat 1-től 100-ig majd irassa ki a számok gyökét, és négyzetét'''

#megoldas
lista = [szam for szam in range(101)if szam %2 == 0]
print(lista)

for szam in lista:
    print(szam ** 0.5)

for szam in lista:
    print(szam ** 2)
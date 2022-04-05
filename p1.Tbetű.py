'''
A  ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python'] lista elemei közül a program kiírja a "t" és "T" betűkkel kezdődőeket!
########################################################################################################################################
Az előző programot alakítsd át úgy, hogy a feltételeknek megfelelő szavak kerüljenek rögzítésre egy másik listában is, és ez utóbbi listát írja ki a program a képernyőre!
'''
lista1=[]
lista2=[]
lista = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']

for i in lista:
    if i[0] == 't' or i[0] == 'T':
        lista1.append(i)
        lista2.append(i)
print(lista2)

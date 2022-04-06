'''
A  ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python'] lista elemei közül a program kiírja a "t" és "T" betűkkel kezdődőeket!
'''
t_betu=[]
lista = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']

for i in lista:
    if i[0] == 't' or i[0] == 'T':
        t_betu.append(i)
print(t_betu)

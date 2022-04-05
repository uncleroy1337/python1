'''
Készíts egy programot, amely a felhasználótól számokat kér be mindaddig, amíg az 'X'-et vagy 'x'-et nem üt! A számokat tárolja el a program egy listában! 
Az adatbekérés befejezte után írja ki a program a lista elemeit, a legkisebb és a legnagyobb számot!
'''

lista = []
while True:
    szam = input("Kérek egy számot: ")
    if szam != "x":
        lista.append(szam)
    else:
        lista.sort(key = int)
        print(lista)
        break
print("a legnagyobb szám: ", max(lista), "a legkissebb szám a", min(lista),"a lista pedig: ", lista)

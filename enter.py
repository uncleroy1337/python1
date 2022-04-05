'''
Készíts egy programot, amely a felhasználótól számokat kér be mindaddig, amíg az csupán ENTER-t nem üt! A számokat tárolja el a program egy listában! Az adatbekérés befejezte után írja ki a program a lista elemeit, a legkisebb és a legnagyobb számot!
'''

lista = []
folytatja = True
while folytatja:
    bekeres = input("Kérek egy számot\t")
    if bekeres != "":
        lista.append(int(bekeres))
    elif bekeres == "":
        folytatja = False

print(f"lista elemei: {lista}")
print(f"legkisebb: {min(lista)} legnagyobb: {max(lista)}")

'''
Készíts egy programot, amely a felhasználótól számokat kér be mindaddig, amíg az csupán ENTER-t nem üt! A számokat tárolja el a program egy listában! Az adatbekérés befejezte után írja ki a program a lista elemeit, a legkisebb és a legnagyobb számot!
'''

lista = []
folytatja = True
while folytatja:
  bekeres = int(input("Kérek egy számot\t"))
  lista.append(bekeres)
  print(lista)
  if bekeres == "":ENTER
    folytatja = False

print(f"lista elemei: {lista}")
print(f"legkisebb: {min(lista)} legnagyobb: {max(lista)}")

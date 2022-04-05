'''
2. Feladat
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!
'''

import random
lista = ["fej", "írás"]
valasztas = random.choice(lista)
print(valasztas)


beker = input("Fej vagy írás? ")

if valasztas == beker:
  print("Nyertél!!")

else:
  print("Próbáld újra!")

'''
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!
'''

import random

random.seed()

def f(i):
    print("%d. feladat" % i)

def egydobas():
    return random.choice('FI')
    
tipp = input('Tippeljen! (F/I)= ')
dob = egydobas()
print('A tipp %s, a dobás eredménye %s volt.' % (tipp, dob))
print('Ön eltalálta.' if tipp == dob else 'Ön nem találta el.')

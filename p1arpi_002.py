'''
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! 
Azután a program bekér egy számot a felhasználótól, majd kiírja,
hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.
'''
import random
i1 = int(input('gondoltam egy szamra, talald ki!: '))
i2 = random.randint(0,5)

if i1 < i2:
    print('a gondolt szám nagyobb mint amit megadtál')
elif i1 > i2:
    print('a gondolt szám kissebb mint amit megadtál')
else:
    print('a gondolt szam egyenlo azzal55 amit megadtál')
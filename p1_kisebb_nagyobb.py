"""
Kérjen be a felhasználotol két egész számot (int) és tárolja el őket. írja ki, hogy melyik a nagyobb és melyik a kisebb szám! Ha két szám egyenlő, akkor azt is jelezze!


Minta:    (output)

1. feladat: Kisebb-nagyobb meghatározása
Kérem az első számot: 12
Kérem az második számot: 3
A nagyobb szám 12, a kisebb 3.



1. feladat: Kisebb-nagyobb meghatározása
Kérem az első számot: -1
Kérem az második számot: 16
A nagyobb szám 16, a kisebb -1.


1. feladat: Kisebb-nagyobb meghatározása
Kérem az első számot: 8
Kérem az második számot: 8
A két szám egyenlő.

"""

# lehetséges megoldás

print('1. feladat: Kisebb-nagyobb meghatározása')
a = int(input('Kérem az első számot: '))
b = int(input('Kérem az második számot: '))
if a > b:
    print(f"A nagyobb szám {a}, a kisebb {b}")
elif b > a:
    print(f"A nagyobb szám {b}, a kisebb {a}")
else:
    print('A két szám egyenlő.')

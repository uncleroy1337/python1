'''
Írj egy programot, ami addig kér be egész pozitív számokat, amíg a felhasználó negtív számot nem ír! 
A megadott számokat tárolja a program egy listában, és ezt adja át paraméterként egy függvények, amely a lista legkisebb elemével tér vissza. 
A program írja ki, hogy melyik volt a megadott legkisebb szám!
'''
szamok = []
while True:
    beker = int(input('adj egy szamot (negatívat a megszakitashoz): '))
    if beker > 0:
        szamok.append(beker) 
    else:
        break

def kissebb(szamok):
    return f'a legkissebb szam {min(szamok)}'

print(kissebb(szamok))

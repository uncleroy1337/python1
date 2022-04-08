'''
Készíts egy programot, amely a felhasználótól számokat kér be mindaddig, amíg az 'X'-et vagy 'x'-et nem üt! A számokat tárolja el a program egy listában! 
Az adatbekérés befejezte után írja ki a program a lista elemeit, a legkisebb és a legnagyobb számot!
'''
lista = []
while True:
        szamok = input("Kérek egy számot: ")
        if szamok == "x" or szamok == "X":
            break
        else:
            lista.append(szamok)
print(f"Legkissebb: {min(lista)} Legnagyobb: {max(lista)}")
            

'''
Írj egy programot, amely szótárban tárolja egy macska nevét, korát. 
A felhasználónak legyen lehetősége megváltoztatni az egyik tárolt adatot. 
A program írja ki a felhasználó választása alapján az egyik adatot, kérdezze meg, mire módosítsa, végül írja ki a képernyőre a frissített adatszerkezetet!
'''

macskaadatok= {
    'név': 'macska',
    'kor': 5,
}


beker = input('Melyik adatot szeretnéd megváltoztatni? (név/kor):  ')
if beker == "név":
    macskaadatok['név'] = input('Mire szeretnéd módosítani?: ')
    macskaadatok.get('név')
    print(macskaadatok)



if beker == "kor":
    macskaadatok['kor'] = input('Mire szeretnéd módosítani?: ')
    macskaadatok.get('kor')
    print(macskaadatok)

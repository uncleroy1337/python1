'''
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! 
A program tartalmazza a függvény hívását is!
'''
 
def harommal_oszthatok(*nums):
    return len([num for num in nums if num % 3 == 0])

   
print(harommal_oszthatok(1,3,9,18,12,40,10,21))

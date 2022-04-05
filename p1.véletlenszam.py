'''
Készíts egy rövid programot, amely 1 és 10 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal! A bekérés addig folytatódjon ameddig a felhasználó nem ad meg negatív számot! Az összehasonlítás eredményéről tájékoztassa a felhasználót!
'''

import random

general = random.randint(1, 10)

while True:
    beker = int(input(f'Kérek egy számot: '))
    if beker == general:
        print(f'Eltaláltad')
        break    
    else:
      print(f'Nem találtad el')

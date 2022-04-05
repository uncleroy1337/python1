'''
A program számolja össze, hogy hány darab 'E' vagy 'e' betűt tartalmazó szó van a szavak listában. 
A képernyőre írja is ki a feltételnek megfelelő szavakat!
'''

szavak = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']
eszavak = []
for valami in szavak:
    if 'e' in valami or 'E' in valami:
        eszavak.append(valami)

print(f'a következő szavak tartalmaznak E/e betűt: {eszavak}')

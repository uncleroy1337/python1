'''
A program tároljon el egy szót egy változóban. A felhasználó adjon meg egy betűt, 
amiről a program döntse el, hogy előfordul-e a szóban! 
Az eredményről tájékoztassa a felhasználót, és írja ki a tárolt szót is!
   
A felhasználónak többször is legyen lehetősége újabb tippet megadnia. A bekérés addig folytatódjon, 
amíg a felhasználó nem ad meg betűt, csupán egy ENTER-t üt!   

Igyekezz minél felhasználóbarátabbá tenni a programot! A programnak lehetnek egyéb hasznos funkciói, 
például gyűjtheti és kiírhatja a jó és a rossz tippeket (betűket).

'''

#megoldas

szo = "python"
print(szo, "\n")

jo_lista = []
rossz_lista = []

while True:
  betu = input("Kérek egy betűt:")
  if betu == "":
    break
  else:
    if betu in szo:
      jo_lista.append(betu)
    else:
      rossz_lista.append(betu)

print(f'Jó tippek: {jo_lista}')
print(f'Rossz tippek: {rossz_lista}')

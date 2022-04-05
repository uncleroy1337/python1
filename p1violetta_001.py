''' 
A program kérjen be két szót a felhasználótól, majd írja ki, 
hogy melyik a hosszabb illetve azt is ha a két szó egyenlő! 

'''

#megoldas

szo1 = input("Adj meg egy szót!")
szo2 = input("Adj meg egy másik szót!")

if len(szo1) > len(szo2):
  print(f'A hosszabb szó:{szo1}')
elif len(szo1) == len(szo2):
  print(f'A két szó egyforma hosszú.')
else:
  len(szo2) > len(szo1)
  print(f'A hosszabb szó:{szo2}')

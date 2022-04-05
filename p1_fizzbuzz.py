#1.nehézségi python feladat
"""
Hozzon létre egy számsorozatot 0-tól 100-ig,
ami 3-mal osztható annál írja ki, hogy 'Fizz'
ami 5-tel osztható annál írja ki, hogy 'Buzz'
ami 3-mal és 5-tel is osztható annál írja li, hogy 'FizzBuzz'
Ami se 3-mal se 5-tel nem osztható annál írjuk ki a magát a számot!
"""

"""Minta: (az első 10 sor output)

FizzBuzz
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz

"""


#lehetséges megoldás

for szam in range(101):
  if szam % 3 == 0 and szam % 5 == 0:
    print("FizzBuzz")
  elif szam % 3 == 0:
    print("Fizz")
  elif szam % 5 == 0:
    print("Buzz")
  else:
    print(szam)

# program losuje liczbe całkowitą 0 - 10
# uzytkownik zgaduje liczbe
# progam pisze, czy liczba podana
# przez uzytkoniwka jest za mala, za duza, czy ok
# max 5 prob

# from random import *    # wszystkie funkcje z biblioteki
# number = randint(0, 10)
# print(f'Wylosowana liczba to {number}')
#
# from random import randint, seed    # konkretne funkcje
# number = randint(0, 10)
# print(f'Wylosowana liczba to {number}')

import random    # biblioteka
_min = random.randint(-100, 0)
_max = random.randint(1, 100)
number = random.randint(_min, _max)
print(f'Wylosowana liczba to {number}')
while True:
    choice = int(input('Zgadnij liczbe:   '))
    if choice < number:
        print('Za malo')
    elif choice > number:
        print('za duzo')
    else:
        print('Ok')
        break

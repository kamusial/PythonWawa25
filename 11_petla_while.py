haslo = '1234'

podane_haslo = input('Podaj haslo:    ')
while haslo != podane_haslo:
    print('haslo niepoprawne, jeszcze raz')
    podane_haslo = input('Podaj haslo:    ')
print('Haslo poprawne')

i = 5
x = 0
while x < i:
   print('Leci petla')
#   x = x + 1
   x += 1
print('koniec programu')



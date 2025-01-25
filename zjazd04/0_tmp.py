a = int(input('Podaj liczbe:  '))
b = int(input('Podaj liczbe:  '))

try:
    wynik = a / b
except:
    print('Nie mogę podzielićprzez zero')


print(wynik)


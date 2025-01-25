try:
    liczba_punktow = int(input('Ile masz punktow?  '))
    wiek = int(input('Ile masz lat?   '))
    poziom = liczba_punktow / wiek
    imie = input('Jak masz na imie?  ')
    print(imie[6])
    with open('dane', 'w') as file:
        file.write('nowa linia')
except ValueError:
    print('Niepoprawny format wprowadzonych danych')
    liczba_punktow = 1
    wiek = 100
except ZeroDivisionError:
    print('wiek nie może być zerem')
    wiek = 100
except IndexError:
    print('Brak danego elementu')
    raise
except FileNotFoundError:
    open('dane', 'w')
    with open('dane', 'w') as file:
        file.write('stworzono plik automatycznie')
        file.write('nowa linia')



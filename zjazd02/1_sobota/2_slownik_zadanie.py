# dane = ['imie', 'nazwisko', 'wiek']
#
# for dana in dane:
#     name = input(f'Podaj {dana}:    ')
#
# print(name)

# program, który przyjmie dane dla X pracowników
# program zwraca słownik {id: słownik danych}

pracownicy = {}
id = 0

while True:
    dane = input('Podaj dane (imie, nazwisko, wiek):   ').split()
    pracownik = {'imie': dane[0], 'nazwisko': dane[1], 'wiek': dane[2]}
    id += 1
    pracownicy[id] = pracownik

    nastepny = input('Czy chcesz dodać kolejną osobę?  T/N ')
    if nastepny[0].lower() != 't':
        break

for id, dane in pracownicy.items():
    print(f'Pracownik o id {id} --- {dane}')

print(pracownicy[1]['nazwisko'])
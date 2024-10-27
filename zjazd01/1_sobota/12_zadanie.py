# napisz program, który przyjmuje tekst (string) i zwraca liczbę samogłosek w tekśice

samogloski = 'aeiouyAEIOUY'

tekst = input('Wpisz tekst:    ')
licznik = 0
for i in range(len(tekst)):
    if tekst[i] in samogloski:
#        licznik += 1
        licznik = licznik + 1
print(f'Liczba samoglosek wynosi {licznik}')

# program która przyjmuje listę i zwraca nową listę z elementami w odwróconej kolejności.
# Użyj pętli while.
odwrocona = []
lista = ['piesek', 'drugi piesek', 'trzeci piesek']
indeks = len(lista) - 1
while indeks >= 0:
    odwrocona.append(lista[indeks])
    indeks -= 1

# program pozwala wprowadzać uzytkownikow i hasła do systemu - max 5
# za każdym razem program pyta, czy wprowadzic kolejnego uzytkownika i haslo
# program potwierdza poprawnosc hasła poprzez dwukrotne wpisanie hasła

users = []
passwords = []
licznik = 0
decyzja = input('Czy chcesz wprowadzic dane uytkownika? t/n ')
while decyzja == 't' and licznik < 5:
    licznik += 1
    user = input('Podaj nazwe uzytkownika:    ')
    passwd = input('Podaj haslo:   ')
    users.append(user)
    passwords.append(passwd)
    decyzja = input('Czy chcesz wprowadzic kolejnego uzytkownika? t/n ')



# program pyta o zarobki, liczbę dzieci i liczbę zwierząt
# na 3cie i kolejne dziecko mamy 800+
# zwierzak kosztuje 300zł
# prograz zwraca informację o dochodzie na głowę w rodzinie

zarobki = float(input('Ile zarabiasz?  '))
liczba_dzieci = int(input('Ile masz dzieci?  '))
liczba_zwierzat = int(input('Ile masz zwierząt?  '))

if liczba_dzieci == 3:
    kasa_total = zarobki + (liczba_dzieci - 2) * 800 - liczba_zwierzat * 300
else:
    kasa_total = zarobki - liczba_zwierzat * 300

kasa_na_glowe = kasa_total / (liczba_dzieci + 2)

print(f'W rodzinie jest {liczba_dzieci+2} osób, w tym {liczba_dzieci} dzieci oraz {liczba_zwierzat} zwierzat.\nNa osobe przypada {round(kasa_na_glowe, 2)} zlotych')
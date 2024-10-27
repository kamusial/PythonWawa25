napis = input('Podaj nazwe:  ')
print(f'{napis} ma {len(napis)} liter.')

licznik_a = 0
licznik_b = 0
for i in range(len(napis)):
    print(f'i wynosi: {i}')
    print(f'Litera {i+1} to {napis[i]}')
    if napis[i] == 'a':
        licznik_a = licznik_a + 1
    if napis[i] == 'b':
        licznik_b = licznik_b + 1
print(f"Litera 'a' wystepuje {licznik_a} razy")
print(f'Litera "b" wystepuje {licznik_b} razy')

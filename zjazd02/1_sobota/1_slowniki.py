lista_zakupow = ['marchew', 3,  'ryz', 5, 'woda', 3]
# lista_zakupow2 = [['marchew', 3],  ['ryz', 5], ['woda', 3]]
# print(lista_zakupow2[1][1])
# lista_zakupow2.append(['marchew', 4])
# print(lista_zakupow2)

slownik_zakupow = {'marchew': 3, 'ryz': 5, 'woda': 3}
print(slownik_zakupow)
# print(slownik_zakupow[2])
print(slownik_zakupow['marchew'])
slownik_zakupow['serek'] = 4
slownik_zakupow['marchew'] = 1
print(slownik_zakupow)
slownik_zakupow['marchew'] += 1

# for produkt in lista_zakupow:
#     print(produkt)

for produkt in slownik_zakupow:      # klucze
    print(f' chcez kupić {produkt} w ilości {slownik_zakupow[produkt]}')

for produkt in slownik_zakupow.keys():
    print(f' chcez kupić {produkt} w ilości {slownik_zakupow[produkt]}')

for cena in slownik_zakupow.values():
    print(cena)

for produkt, cena in slownik_zakupow.items():   #wszystko
    print(f'kupujesz {produkt} w liczbie {cena}')



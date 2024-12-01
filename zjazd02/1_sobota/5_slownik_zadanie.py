ceny_lidl = {'marchew': 4, 'miod': 9.9, 'chleb': 3.2, 'mleko': 4.2, 'jablko': 0.99}
ceny_aldi = {'marchew': 2, 'miod': 19.9, 'chleb': 5.2, 'mleko': 1.2, 'jablko': 4.2}
ceny_dino = {'marchew': 1.93, 'miod': 4.99, 'chleb': 3.9, 'mleko': 2.23, 'jablko': 7.99}

zakupy = {'marchew': 6, 'chleb': 2, 'mleko': 6, 'jablko': 14, 'miod': 3}

suma_lidl = 0
for produkt in zakupy.keys():
    suma_lidl += ceny_lidl[produkt]

print(f'W lidlu zapłacisz {suma_lidl} zł')
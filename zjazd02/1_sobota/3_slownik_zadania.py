# dany jest słownik  dostępnych w domu
dostepne = {'mleko': 5, 'jajko': 12, 'maka': 4, 'maslo': 2, 'woda': 10}

# dany jest słownik produktow potrzebnych do upieczenia ciasta
ciasto = {'jajko': 4, 'maka': 0.5, 'maslo': 0.6, 'mleko': 1.9}

# program liczy, ile ciast można upiec z dostępnych składników i pokaże krytyczny składnik

liczba_ciast = 9999
for skladnik in ciasto:
    if dostepne[skladnik] // ciasto[skladnik] < liczba_ciast:
        liczba_ciast = dostepne[skladnik] // ciasto[skladnik]
print(f'Można upiec: {liczba_ciast}')



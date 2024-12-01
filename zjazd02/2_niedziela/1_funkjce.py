def przywitanie():
    print('Siema')


def przywitanie2(imie):
    print(f'cześć {imie}')


def przywitanie3(imie, wiek, plec):
    if wiek < 18:
        print(f'Siema {imie}')
    else:
        if plec[0].lower() == 'k':
            print(f'Dzień dobry Pani {imie}')
        else:
            print(f'Dzień dobry Pan {imie}')


przywitanie()
przywitanie2('Kamil')
przywitanie3('Anna', 21, 'k')

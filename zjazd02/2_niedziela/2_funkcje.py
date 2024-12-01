def stawka_ubezpieczenia(wiek, waga, czy_pali):
    stawka_bazowa = 200
    if wiek > 50:
        stawka_bazowa += wiek
    if waga > 100:
        stawka_bazowa += waga
    if czy_pali:
        stawka_bazowa *= 2
    return stawka_bazowa


ubezpieczenie_kamil = stawka_ubezpieczenia(36, 90, False)
print(f'Kamil zapłaci {ubezpieczenie_kamil}')


def ubezpieczenie_zwierzecia(typ, wiek):
    print(f'zwierze: {typ} w wieku {wiek} lat')
    if typ == 'pies':
        return (100 * 1.5) + (wiek - 5) * 10
    return (200 * 1.2) + (wiek - 7) * 8

print(f'zaplacisz: {ubezpieczenie_zwierzecia("pies", 12)}')



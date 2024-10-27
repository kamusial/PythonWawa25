item = input('Podaj daną:  ')

try:
    item = int(item)
    print('Wpisana dana została skonwertowana do INT')
except:
    try:
        item = float(item)
        print('Wpisana dana została skonwertowana do FLOAT')
    except:
        print('Nie udało się rzutowanie do INT, ani FLOAT\nzostaje STR')
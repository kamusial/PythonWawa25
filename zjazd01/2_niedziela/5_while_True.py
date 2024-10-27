my_list = []

while True:
    product = input('Podaj produkt:  ')
    my_list.append(product)
    decision = input('czy chcesz dodac kolejny produkt?  y/n  ')
    if decision == 'n':
        break    # wyjscie z petli

print('dalsza czesc programu')
print(my_list)
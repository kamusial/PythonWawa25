my_list = []
variable = 1

while variable == 1:
    product = input('Podaj produkt:  ')
    my_list.append(product)
    decision = input('czy chcesz dodac kolejny produkt?  y/n  ')
    if decision == 'n':
        variable = 2

print('dalsza czesc programu')
print(my_list)
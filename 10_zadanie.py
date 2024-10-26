lista_imion = ['Wioleta', 'Monika', 'Dawid', 'Patryk', 'Magda']

print(len(lista_imion))
men = []
women= []

for i in range(len(lista_imion)):
    print(lista_imion[i])
    if lista_imion[i][-1] != 'a':
        print('Witam Pana')
        men.append(lista_imion[i])
    else:
        print('Witam Pania')
        women.append(lista_imion[i])


# napisać spersonalizowane powitanie dla Pań i Panów
# zapisać ludzi w osobnych listach

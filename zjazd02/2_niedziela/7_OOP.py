czlowiek_1 = [324623, 'Kamil', 'mail@mail.com', 22]
czlowiek_2 = [362423, 'Kamil', 'mail@mail.com', 3]
czlowiek_3 = [324523, 'Kamil', 'mail@mail.com', 4]
people_list = []
people_list.append(czlowiek_1)
people_list.append(czlowiek_2)
people_list.append(czlowiek_3)

print(people_list)

def dodaj_urlop(czlowiek, ile):
    if czlowiek[3] >= ile:
        czlowiek[3] -= ile
    else:
        print('Brak mozliwosci')

dodaj_urlop(people_list[1], 5)
print(people_list[1])

nazwa = 'piesek'
zmienna = 5
people = int(input('Ilu jest ludzi?   '))
total_money = float(input('Ile jest w sumie pieniedzy?   '))

try:
    money_per_person = total_money / people
except:
    print('Blad, zakladam 2 osoby')
    money_per_person = total_money / 2



print(f'Kasa na glowe: {money_per_person}')

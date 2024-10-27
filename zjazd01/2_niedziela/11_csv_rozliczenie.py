# 1. Oczyt pliku csv z zapisem poszczególnych pól

# with open ('rozliczenie.csv', 'r')
file = 'rozliczenie.csv'
mode = 'r'
with open(file, mode) as moje_rozliczenie:
    content = moje_rozliczenie.readlines()
#    print(content)

for i in range(len(content)):
#    print(f'przed: {content[i]}')
    content[i] = content[i].replace('\n','',1)
    content[i] = content[i].split(',')

#    print(f'po: {content[i]}')

print(content)   # cała lista list
print(content[4]) # jedna linia
print(content[4][2])  # jedna komórka
print(content[0][2][2:5])   # kawałek stringa, napisu

total_money = 0
# 2. Obliczanie średniej wypłaty
for person in content[1:]:
    print(person[1])
    total_money += float(person[1])
print(f'Srednia wyplata: {round(total_money / (len(content)-1),0)}')

# for i in range(1, len(content)):
#     print(content[i][1])
#     total_money += float(content[i][1])

# 3. Ile kobiet na macierzynskim

counter_maternity = 0
for person in content[1:]:
#    print(person[4])
    if person[4][0].lower() == 't' and person[3] == 'k':
        counter_maternity += 1
print(f'Liczba pań na macierzynskim: {counter_maternity}')
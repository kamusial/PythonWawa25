# program przyjmuje dowlnie długą liczbę i zwraca sumę cyfr

while True:
    try:
        number = int(input('Podaj liczbe:  '))
        break
    except:
        print('Jeszcze raz')

str_number = str(number)   # zamiana na stringa
sum = 0
for digit in str_number:
    sum += int(digit)
print(sum)
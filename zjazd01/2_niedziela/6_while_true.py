# program przyjmuje inty od 1 do 10
# max 5 prob

counter = 0
while True:
    number = int(input('Podaj liczbe:  '))
    if 0 < number <= 10:
        break
    counter += 1
    if counter == 5:
        print('Przekroczono limit 5ciu prob')
        break

print('Dalsza czesc programu')
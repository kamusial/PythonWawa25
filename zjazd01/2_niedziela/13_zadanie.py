# sprawdź, czy wprowadzone słowo jest anagaram
# sprawdź to dla listy wprowadzonych slow

word = input('Podaj slowo:   ')
no_of_iterations = len(word) // 2    # czesc calkowita z dzielenia

for i in range(no_of_iterations):
    if word[i] != word[-1-i]:
        print('nok')
        break

# prostrzy sposob
if word == word[::-1]:
    print('ok')
else:
    print('nok')


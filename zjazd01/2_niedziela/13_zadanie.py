# sprawdź, czy wprowadzone słowo jest anagaram / palindrom
# sprawdź to dla listy wprowadzonych slow

word = input('Podaj slowo:   ')
# word = word.replace(' ','').lower()
no_of_iterations = len(word) // 2    # czesc calkowita z dzielenia

for i in range(no_of_iterations):
    if word[i] != word[-1-i]:
        print('nok')
        break

# prostrzy sposob
if word.replace(' ','').lower() == word[::-1].replace(' ','').lower():
    print('ok')
else:
    print('nok')


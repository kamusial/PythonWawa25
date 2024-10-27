wiek = int(input('Ile masz lat?   '))
print(f'Masz {wiek} lat.')
if wiek < 18:
    print(f'Bedziesz dorosly za {18 - wiek} lat.')
elif wiek == 18:
    print('Jestes dorosly w Europie, ale uwazaj.')
elif wiek < 21:
    print('Jestes dorosly w Europie, a w USA nie')
else:
    print('Jestes dorosly wszedzie.')

print('Dalsza czesc programu')

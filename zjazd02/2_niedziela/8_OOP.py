class Czlowiek:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.mail = name+'@firma.com'
        self.urlop = 15

    def wykorzystaj_urlop(self, ile):
        if self.urlop >= ile and ile > 0:
            self.urlop -= ile
        else:
            print('Złe dane')

    def dodaj_urlop(self, ile):
        passwd = input('Podaj haslo: ')
        if passwd == 'abc':
            print('Mail wysłany do managera')
            self.urlop += ile
            print(f'Mail do {self.name}')


pracownik1 = Czlowiek(999, 'Marek')
print(pracownik1.name)
print(pracownik1.urlop)
pracownik1.wykorzystaj_urlop(10)
print(pracownik1.urlop)

pracownik2 = Czlowiek(50, 'Kasia')
print(pracownik2.dodaj_urlop(30))




class Auto:
    def __init__(self, kolor, stan, wiek):
        self.kolor = kolor
        self.stan = stan
        self.ilosc_paliwa = 10
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        self.rocznik = 2024 - wiek

    def __str__(self):
        return f'Pojazd w stanie {self.stan} z rocznika {self.rocznik}'

    def zasieg(self):
        zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100 * 0.9
        return round(zasieg)

    def ustaw_tryb(self, tryb):
        if tryb == 'eco':
            self.tryb_ekonomiczny = True
            self.spalanie_na_100 = 10
        elif tryb == 'normal':
            self.tryb_ekonomiczny = False
            self.spalanie_na_100 = 14
        else:
            print('bez zmian')


auto01 = Auto('black', 4, 12)
print(f'spalanie wynosi {auto01.spalanie_na_100}')
print(auto01)
print(auto01.zasieg())
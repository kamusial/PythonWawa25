"""
Liczba numerologiczna:
1992-02-15:
1+9+9+2 + 0+2 + 1+5   =  29
29:
2+9 = 11
11:
1+1 = 2

Oblicz cyfrę numerologiczną dla osoby urodzonej 10000 dni temu.
"""
from datetime import datetime, timedelta

today = datetime.today()

date_before = today - timedelta(days=10000)

format_date = int(date_before.strftime('%Y%m%d'))
digit_sum = sum(int(digit) for digit in str(format_date))

while len(str(digit_sum)) >= 2:
    digit_sum = sum(int(digit2) for digit2 in str(digit_sum))
print(digit_sum)

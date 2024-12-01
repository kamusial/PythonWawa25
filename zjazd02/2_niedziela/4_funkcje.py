def net_salary(age, gross_salary=3000, year=2024):
    if age < 26:
        return f'w roku {year} wyplata wynosi {gross_salary}'
    else:
        return f'w roku {year} wyplata wynosi {gross_salary*.8}'


print(net_salary(year=2021, age=5000))
print(net_salary(43, 100))



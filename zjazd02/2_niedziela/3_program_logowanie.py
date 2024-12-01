# import time
#
# for _ in range(5):
#     print('siema')
#     time.sleep(1)

import funkcje_3
# print(f'{funkcje_3.passwd_length("Kamil123")}')

name = input('Podaj nazwę użytkownika:  ')
if funkcje_3.user_exist(name):
    counter_passwd = 0
    print(f'Witaj {name}')
    while True:
        passwd = input('Podaj hasło:  ')
        if funkcje_3.passwd_correct(name, passwd):
            break
        else:
            print('Zle haslo, jeszcze raz:  ')
            counter_passwd += 1
            if counter_passwd == 3:
                import sys
                sys.exit(0)

    print('Jestes zalogowany')

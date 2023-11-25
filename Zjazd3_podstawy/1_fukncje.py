def przywitaj():
    print('...............')
    print('Witamy na spotkaniu')
    print('plik z logami uaktualniony')


def przywitaj_spersonalizowane1(x):
    print('Siema ',x)
    print(f'Siema {x}')

while True:
    decision = input("Czy przywitać? T/N ")
    if decision.lower() == 't':
        przywitaj()
    else:
        print("Brak przywitania")
        break

imie = input('Podaj imie: ')
przywitaj_spersonalizowane1(imie)

def welcome(imie, wiek):
    if wiek <= 20:
        print(f'cześć {imie}')
    elif wiek > 20 and imie[-1] == 'a':
        print(f'Dzień dobry Szanowna Pani {imie}')
    else:
        print(f'Dzień dobry Szanowny Panie {imie}')



username = input('podaj imie: ')
age = input('podaj wiek: ')

welcome(username, age)


def pobierz_informacje(nr_konta):
    if nr_konta in Imiona and nr_konta in stan_konta:
        imie = Imiona[nr_konta]
        stan = stan_konta[nr_konta]
        print(f'Informacje dla konta o numerze {nr_konta}:')
        print(f'Imię: {imie}')
        print(f'Stan konta: {stan}')
    else:
        print('Brak informacji dla podanego numeru konta.')

Imiona = {
    4123: 'Asia',
    1234: 'Kamil',
    8777: 'Bartosz'
}

stan_konta = {
    4123: 2342,
    1234: 0,
    8777: 100000
}

while True:
    try:
        numer_konta = int(input('Podaj numer konta (lub wpisz 0, aby zakończyć): '))
        if numer_konta == 0:
            break
        pobierz_informacje(numer_konta)
    except ValueError:
        print('Nieprawidłowy format numeru konta. Spróbuj ponownie.')
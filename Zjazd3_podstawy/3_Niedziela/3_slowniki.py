# napisz program, który przyjmuje numer i zwraca wszystkie dostępne informacje
# napisz program, który przyjmuje imie i zwraca stan konta

imiona = {
    4123: 'Asia',
    1234: 'Kamil',
    8777: 'Bartosz'
}

stan_konta = {
    4123: 2342,
    1234: 0,
    8777: 100_000
}

print(imiona)
print(stan_konta)

def check_account_func():
    account = int(input("Jaki numer konta chcesz sprawdzić?: "))
    if account in imiona:
        print(account, imiona[account], stan_konta[account])

check_account_func()

# def check_account_func():

#     check_acct_number = input("Podaj numer konta: ")
#     if check_acct_number in imiona:
#         print(f"Oto informacje o Twoim koncie: Imię: {imiona.get(check_acct_number)}")
#
#
# check_account_func()

# for i in imiona:
#     if imiona.key[i] in stan_konta.keys():
#         print(i)
#
# # def all_info():
#     for i in imiona:
#         print(i)

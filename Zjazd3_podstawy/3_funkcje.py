# funkcja, która przyjmuje wiek auta, liczbe skód, wiek kierowcy
# funkcja mówi, ile będzie kosztować składka na ubezpieczenie

def wysokosc_skladki(wiek_auta, liczba_szkod, wiek_kierowcy):
    skladka = 0
    skladka += wiek_auta * 20
    skladka += liczba_szkod * 200
    if wiek_kierowcy < 25:
        skladka += 100
    print(f'skladka wynosi {skladka}')
    return skladka


wysokosc_skladki(wiek_auta=10, liczba_szkod=2,wiek_kierowcy=30)

czynsz = 500
jedzenie = 700

#!/bin/env python3
def oblicz_sume(cyfry,wagi,modulo=10):
    cyfry_z_wagami = zip(cyfry,wagi)
    cyfry_wazone = [c*w for c,w in cyfry_z_wagami]
    return sum(cyfry_wazone) % modulo

def sprawdz_pesel(cyfry):
    sk = oblicz_sume(cyfry, (9,7,3,1,9,7,3,1,9,7,0) )
    return cyfry[10] == sk

def sprawdz_nip(cyfry):
    sk = oblicz_sume(cyfry, (6,5,7,2,3,4,5,6,7,0), 11)
    return cyfry[9] == sk

def sprawdz_regon(cyfry):
    sk = oblicz_sume(cyfry, (8,9,2,3,4,5,6,7,0), 11)
    return cyfry[9] == sk

if __name__ == '__main__':
    while True:
        numer = input('Podaj numer do sprawdzenia albo \
nacisnij ENTER aby wyjsc: ')
        if not numer:
            break
        cyfry = [int(cyfra) for cyfra in numer.replace('-','')]
        if len(cyfry) == 11:
            rodzaj = 'PESEL'
            wynik = sprawdz_pesel(cyfry)
        elif len(cyfry) == 10:
            rodzaj = 'NIP'
            wynik = sprawdz_nip(cyfry)
        elif len(cyfry) == 9:
            rodzaj = 'REGON'
            wynik = sprawdz_regon(cyfry)
        else:
            raise ValueError('Nieznany format danych!')
        if wynik:
            print('Numer {} jest poprawny.'.format(rodzaj))
        else:
            print('Numer {} jest bledny.'.format(rodzaj))
    

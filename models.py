import randoms
import string
import random

ilosc_roli = 3 #DONE
ilosc_karetek = 100 #DONE
ilosc_pracownikow = 350 #DONE
ilosc_dyzurow = 5000 #DONE
ilosc_pracownikow_na_dyzurze = 15000 #DONE
ilosc_typow_karetek = 5 #DONE
ilosc_wyposazen = 69 #DONE
ilosc_wyposazen_w_karetce = ilosc_wyposazen * ilosc_karetek #DONE
ilosc_szpitali = 30 #DONE
ilosc_oddzialow_szpitali = 300 #DONE
ilosc_zgloszen = 10000 #DONE
ilosc_poszkodowanych = 20000 #DONE
ilosc_schorzen_poszkodowanego = 30000 #DONE
ilosc_typow_schorzen = 3 #DONE
ilosc_schorzen = 600 #DONE
ilosc_typow_karetek_do_schorzenia = 100 #DONE
ilosc_dyzurow_do_zgloszenia = ilosc_zgloszen * 1.5 #DONE
ilosc_roli_pracownika = ilosc_pracownikow * 1.5 #DONE

def get_pracownik():
    imie = randoms.get_name()
    return (imie, randoms.get_surname(imie), randoms.get_date(1950, 1990))

def get_dyzur():
    td = randoms.get_timedate()
    return (randoms.get_number(0, ilosc_karetek), td, randoms.datetime_after_8_hours(td), randoms.get_random_location())

def get_pracownik_na_dyzurze():
    return (randoms.get_number(0,ilosc_dyzurow), randoms.get_number(0,ilosc_pracownikow), randoms.get_number(0,ilosc_roli))

def get_karetka():
    return ('S', randoms.get_rejestracja(), randoms.get_number(0,2) == 0, randoms.get_date(2018, 2025))

def get_wyposazenie_w_karetce():
    return (randoms.get_number(1, ilosc_wyposazen+1), randoms.get_number(0, ilosc_karetek), randoms.get_number(0,2) == 0)

def get_zgloszenie():
    return (randoms.get_adres(), randoms.get_random_location(), "")

def get_dyzur_do_zgloszenia():
    return (randoms.get_number(0, ilosc_dyzurow), randoms.get_number(0,ilosc_zgloszen))

def get_szpital():
    return (randoms.get_adres(), randoms.get_random_location())

def get_schorzenie():
    return randoms.get_schorzenie()

def get_typy_schorzenia():
    lines = []
    for i in range(ord('A'), ord('Z') + 1):
        lines.append(str(chr(i)))
    return lines

def get_oddzialy_szpitalu():
    return (randoms.get_number(0, ilosc_szpitali), randoms.get_number(0,ilosc_typow_schorzen))

def get_typ_karetki_do_schorzenia():
    #tab = ['K', 'N', 'P', 'S', 'T']
    return ('S', random.choice(string.ascii_uppercase))

def get_poszkodowany():
    return (randoms.get_number(0, ilosc_zgloszen), "", "")

def get_schorzenie_poszkodowanego():
    return (randoms.get_number(0, ilosc_poszkodowanych), randoms.get_schorzenie())

def get_rola_pracownika():
    return (randoms.get_number(0, ilosc_roli), randoms.get_number(0, ilosc_pracownikow))
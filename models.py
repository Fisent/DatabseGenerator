import randoms
import string
import random

def get_pracownik():
    imie = randoms.get_name()
    return (imie, randoms.get_surname(imie), randoms.get_date(1950, 1990))

def get_dyzur():
    td = randoms.get_timedate()
    return (randoms.get_number(0, 500), td, randoms.datetime_after_8_hours(td))

def get_pracownik_na_dyzurze():
    return (randoms.get_number(0,100), randoms.get_number(0,3))

def get_karetka():
    return (randoms.get_number(0,5), randoms.get_rejestracja(), randoms.get_number(0,2) == 0, randoms.get_date(2018, 2025))

def get_wyposazenie_w_karetce():
    return (randoms.get_number(0, 15), randoms.get_number(0, 100))

def get_zgloszenie():
    return ("adres", "pozycja", "opis zgloszenia")

def get_dyzur_do_zgloszenia():
    return (randoms.get_number(0, 5000), randoms.get_number(0,10000))

def get_szpital():
    return ("adres", "pozycja")

def get_schorzenie():
    return (randoms.get_schorzenie())

def get_typ_schorzenia():
    return (randoms.get_typ_schorzenia())

def get_oddzialy_szpitalu():
    return (randoms.get_number(0, 5000), random.choice(string.ascii_lowercase))

def get_typ_karetki_do_schorzenia():
    return (randoms.get_number(0, 5), random.choice(string.ascii_lowercase))

def get_poszkodowany():
    return (randoms.get_number(0, 10000), "", "")

def get_schorzenie_poszkodowanego():
    return (randoms.get_number(0, 20000), randoms.get_schorzenie())
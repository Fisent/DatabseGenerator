import random
import string
from datetime import date, timedelta, datetime


def get_name():
    names = []
    names_f = open("names", mode="r", encoding="UTF-16")
    for line in names_f:
        names.append(line[0:-1])
    return random.choice(names)

def get_surname(name):
    surnames = []
    surnames_f = open("surnames", mode="r", encoding="UTF-16")
    for line in surnames_f:
        surnames.append(line[0:-1])
    sur = random.choice(surnames)
    if name.endswith('a'):
        if(sur.endswith('i')):
            sur = sur[0:-1] + 'a'
        return sur
    else:
        return sur

def get_date():
    start_date = date.today().replace(day=1, month=1, year=2000).toordinal()
    end_date = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_date, end_date))
    return random_day

def get_date(from_year, to_year):
    start_date = date.today().replace(day=1, month=1, year=from_year).toordinal()
    end_date = date.today().replace(year=to_year).toordinal()
    random_day = date.fromordinal(random.randint(start_date, end_date))
    return random_day

#from_num - włącznie, to-num - wyłącznie
def get_number(from_num, to_num):
    return random.randrange(from_num, to_num)

#ostatnie 2 lata
def get_timedate():
    return datetime(year=get_number(2014, 2017), month=get_number(1, 13), day=get_number(1, 29), hour=get_number(0,24), minute=get_number(0,60));

def datetime_after_8_hours(dt):
    return dt + timedelta(hours=8)

def get_rejestracja():
    rejestracja = ""
    for i in range(8):
        rejestracja += random.choice(string.ascii_lowercase)
    return rejestracja

def get_choroba():
    file = open("choroby.txt", mode="r")
    lines = []
    for line in file:
        line = line.strip()
        if line != "":
            lines.append(line)
    return random.choice(lines)

def get_typ_choroby(choroba):
    return 0


<<<<<<< 41e0dab65078e7d3f8a53960831e8fe25abf259b
import models
import randoms

print(models.get_dyzur())
print(models.get_pracownik())
print(models.get_pracownik_na_dyzurze())
print(models.get_karetka())
print(randoms.get_choroba())
=======
import random
import psycopg2
import models

names = []
surnames = []

names_f = open("names",  "r")
surnames_f = open("surnames",  "r")

for line in names_f:
    names.append(line[0:-1])

for line in surnames_f:
    surnames.append(line[0:-1])

def get_name():
    return random.choice(names)[0:-1]

def get_surname(name):
    sur = random.choice(surnames)
    if name.endswith('a'):
        if(sur.endswith('i')): 
	    sur = sur[0:-1] + 'a'
        return sur
    else:
        return sur

for i in range(100):
    name = get_name()
    print(name + " " + get_surname(name))
>>>>>>> commit

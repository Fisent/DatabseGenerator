import random

names = []
surnames = []

names_f = open("names",  "r")
surnames_f = open("surnames",  "r")

for line in names_f:
    names.append(line)
for line in surnames_f:
    surnames.append(line)

def get_surname():
    return random.choice(names)

def get_name():
    return random.choice(surnames)
    
for i in range(100):
    print(get_name() + " " + get_surname())

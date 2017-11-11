import random
import psycopg2

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


try:
    conn = psycopg2.connect("dbname='template1' user='dbuser'm host='localhost' password='pass'")
except:
    print "I am unable to connect to the database"

import psycopg2


def send_lekarz(lekarz):
    try:
        conn = psycopg2.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")
        print conn + " "
    except:
        print "I am unable to connect to the database"


send_lekarz(1)

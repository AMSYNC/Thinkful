import sqlite3 as lite
import pandas as pd
import sys

# per the assignment request to "write input that can be dynamic" I decided to also make the table creation/population process 
# dynamic which allows creating new tables and populating them by adding a new table name, structure, etc to the dictionaries.
# Not sure if this would every be realistic or useful, but I wanted to practice writing dynamic SQL statements

# The code is probably very crappy, because I had a really hard time doing some parts of this. It was also hassle to work with 
# dataframes because I just couldn't figure out how to query them and couldn't find good source to learn it.

tablenames = {1:"cities", 2:"weather"}
tablestructures = {1:" (name text, state text)", 2:" (city text, year integer, warm_month text, cold_month text, average_high integer)"}
tablecolnum = {1:2, 2:5}
values = {1: (('New York City', 'NY'), ('Boston', 'MA'), ('Chicago', 'IL'), ('Miami', 'FL'), ('Dallas', 'TX'), ('Seattle', 'WA'), ('Portland', 'OR'), ('San Francisco', 'CA'), ('Los Angeles', 'CA')), \
          2: (('New York City',2013,'June','January',62),('Boston',2013,'July','January',59),('Chicago',2013,'July','January',59),('Miami',2013,'August','January',84),('Dallas',2013,'July','January',77),('Seattle',2013,'June','January',61),('Portland',2013,'July','December',63),('San Francisco',2013,'September','December',64),('Los Angeles',2013,'September','December',75))}

months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

con = lite.connect("assignment.db")

with con:
    
    cur = con.cursor()
    
    for table in tablenames:
        cur.execute("DROP TABLE IF EXISTS "+str(tablenames[table]))
        cur.execute("CREATE TABLE "+str(tablenames[table])+str(tablestructures[table]))
        cur.executemany("INSERT INTO "+str(tablenames[table])+" VALUES"+"("+((tablecolnum[table])-1)*"?,"+"?)", values[table])

    print "Pick a month and find out the warmest cities to visit!\n"
    print "January  (1)"
    print "February (2)"
    print "March    (3)"
    print "April    (4)"
    print "May      (5)"
    print "June     (6)"
    print "July     (7)"
    print "August   (8)"
    print "September(9)"
    print "October  (10)"
    print "November (11)"
    print "December (12)\n"
    
    while True:
        try:
            choice = raw_input("Please select a month by number: ")
            if int(choice) >= 1 and int(choice) <= 12:
                break
            print "Planet earth does not have such a month... Try again..."    
        except:
            print "Oops!  That was no valid number.  Try again..."
    
    print ""
    cur.execute("SELECT name, state, warm_month FROM cities INNER JOIN weather ON cities.name = weather.city")
    rows = cur.fetchall()
    df = pd.DataFrame(rows, columns=["name", "state", "warm_month"])
    
    choice = int(choice)

    n = df[(df.warm_month == months[choice])]["name"].values
    s = df[(df.warm_month == months[choice])]["state"].values
    
    if len(n) == 0:
        print "Brrr! It's too cold this month, just stay inside!"
    else:
        print "The cities that are warmest in "+months[choice]+" are: " + str(n + ", " +s)[2:-2]
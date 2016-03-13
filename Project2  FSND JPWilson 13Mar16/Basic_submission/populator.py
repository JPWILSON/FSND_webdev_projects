import psycopg2

DB = psycopg2.connect('dbname = tournament')
c = DB.cursor()

c.execute("INSERT INTO players(name) VALUES('J Player1 Wilson');")
c.execute("INSERT INTO players(name) VALUES('R Player2 Beater');")
c.execute("INSERT INTO players(name) VALUES('T Player3 Howard');")
c.execute("INSERT INTO players(name) VALUES('W Player4 Rourke');")
c.execute("INSERT INTO players(name) VALUES('V Player5 Tedds');")
c.execute("INSERT INTO players(name) VALUES('H Player6 Mat');")
c.execute("INSERT INTO players(name) VALUES('U Player7 Willows');")
c.execute("INSERT INTO players(name) VALUES('R Player8 Talbot');")
# Now insert the match results
c.execute("INSERT INTO matches VALUES(1,2);")
c.execute("INSERT INTO matches VALUES(3,4);")
c.execute("INSERT INTO matches VALUES(5,6);")
c.execute("INSERT INTO matches VALUES(8,7);")
c.execute("INSERT INTO matches VALUES(3,1);")
c.execute("INSERT INTO matches VALUES(5,8);")
c.execute("INSERT INTO matches VALUES(2,4);")
c.execute("INSERT INTO matches VALUES(6,7);")
c.execute("INSERT INTO matches VALUES(3,5);")
c.execute("INSERT INTO matches VALUES(1,8);")
c.execute("INSERT INTO matches VALUES(2,6);")
c.execute("INSERT INTO matches VALUES(7,4);")

DB.commit()
DB.close()
import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE Ages ( 
              name VARCHAR(128), 
              age INTEGER
              )""")

c.executescript('''DELETE FROM Ages;
                   INSERT INTO Ages (name, age) VALUES ("Lauchlan", 18);
                   INSERT INTO Ages (name, age) VALUES ("Eriz", 22);
                   INSERT INTO Ages (name, age) VALUES ("Boyd", 28);
                   INSERT INTO Ages (name, age) VALUES ("Anais", 16);
                   INSERT INTO Ages (name, age) VALUES ("Mia", 34);
                   INSERT INTO Ages (name, age) VALUES ("Jaheim", 21);
                ''')

c.execute("""
SELECT hex(name || age) AS X FROM Ages ORDER BY X
""")

print(c.fetchall())

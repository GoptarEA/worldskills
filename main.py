import psycopg2

connect = psycopg2.connect(dbname="Users", user="postgres", password="admin", host="127.0.0.1")
connect.autocommit = True
cur = connect.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
    id serial PRIMARY KEY,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL
);
""")
# connect.commit()
first = "Petya"
second = "Vasiliev"

cur.execute("INSERT INTO users (first_name, last_name) VALUES (%s, %s)", (first, second))

with open('table1.txt') as table:
    for row in table:
        print(row)

cur.close()
connect.close()
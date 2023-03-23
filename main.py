import psycopg2

connect = psycopg2.connect(dbname="Users", user="postgres", password="admin", host="127.0.0.1")
connect.autocommit = True
cur = connect.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS uslugi (
    id serial PRIMARY KEY,
    code varchar(10) NOT NULL,
    title varchar(100) NOT NULL,
    price float(4) NOT NULL
);
""")




with open('table.csv', encoding='utf-8-sig') as table:
    for row in table:
        sp = row.strip().split(";")
        print(sp)
        cur.execute(
            "INSERT INTO uslugi (code, title, price) VALUES (%s, %s, %s)",
            (sp[0], sp[1], float(sp[2].replace(',', '.')))
        )

cur.close()
connect.close()
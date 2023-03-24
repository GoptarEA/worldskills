import psycopg2

connect = psycopg2.connect(dbname="Users", user="postgres", password="admin", host="127.0.0.1")
connect.autocommit = True
cur = connect.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS shops (
    id serial PRIMARY KEY,
    shop_id varchar(50) NOT NULL,
    district varchar(100) NOT NULL,
    address varchar(100) NOT NULL
);
""")

f = open("Магазины.csv", encoding="utf-8")

for row in f:
    sp = row.strip().split(";")
    cur.execute("INSERT INTO shops (shop_id, district, address) VALUES (%s, %s, %s)", (sp[0], sp[1], sp[2]))

cur.close()
connect.close()



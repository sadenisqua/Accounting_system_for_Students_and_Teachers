import psycopg2
from psycopg2.extras import RealDictCursor, execute_values

conn = psycopg2.connect(dbname="testdb", user='postgres', password='7910dk123')

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS superheroes')
cur.execute('DROP TABLE IF EXISTS traffic_light')

conn.commit()

cur.execute("CREATE TABLE superheroes (hero_id serial PRIMARY KEY, hero_name varchar, straight int);")

cur.execute('INSERT INTO superheroes (hero_name, straight) VALUES (%s, %s)', ('Superman', 100))
cur.execute('INSERT INTO superheroes (hero_name, straight) VALUES (%s, %s)', ('Flash', 999))

cur.execute('''
                INSERT INTO superheroes(hero_name, straight)
                VALUES (%(name)s, %(straight)s);
                ''', {'name': 'Green Arrow', 'straight': 80})

conn.commit

cur.execute("CREATE TABLE  traffic_light (light_id serial PRIMARY KEY, light text);")

cur.execute("INSERT INTO traffic_light(light) VALUES (%s)", ('red',))

cur.execute("SELECT * FROM superheroes")

one_line = cur.fetchone()
print(one_line)

full_fetch = cur.fetchall()
for record in full_fetch:
    print(record)


conn.commit()


cur.close()
conn.close()

with psycopg2.connect(dbname="testdb", user='postgres', password='7910dk123') as conn:
    with conn.cursor(cursor_factory=RealDictCursor) as curs:

        execute_values(curs, "INSERT INTO traffic_light (light) VALUES %s", [('green',), ('yellow',)])

        curs.execute("SELECT * FROM traffic_light")
        records = curs.fetchall()
        print(records)
        print(records[0]["light"])

conn = psycopg2.connect(dbname='testdb', user='postgres', password='7910dk123')
try:
    with conn:
        with conn.cursor() as curs:
            curs.execute(""""
                    UPDATE superheroes
                    SET straight = %s
                    """, (90, 'Superman'))
finally:
    curs.close()
    conn.close()


with conn:
    with conn.cursor() as curs:
        curs.execute("SELECT * FROM  superheroes")
        print(curs.fetchall())
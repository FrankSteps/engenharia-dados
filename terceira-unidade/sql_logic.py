import psycopg2 

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="Funcionarios",
    user="postgres",
    password="Pedro27%"
)

with conn.cursor() as cur:
    cur.execute("SELECT current_database(), version();")
    print("Conectado ao banco:", cur.fetchone())

conn.close()

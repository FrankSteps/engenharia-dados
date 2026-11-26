import psycopg2 

# Example
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="Funcionarios",
    user="postgres",
    password=""
)

with conn.cursor() as cur:
    cur.execute("SELECT current_database(), version();")
    print("Conectado ao banco:", cur.fetchone())

conn.close()

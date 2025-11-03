import psycopg2

conn = psycopg2.connect(
    dbname="cooperativa_db2",
    user="cooperativa_db2_user",
    password="cdZsGOGttCq0MW1mqnBJgmNRjPExk1gl",
    host="dpg-d449m79r0fns7381ubcg-a.render.com",
    port="5432"
)

print("Conexão bem-sucedida!")
conn.close()
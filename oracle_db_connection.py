import cx_Oracle
import json
 
 
with open ('login.json', 'r') as arquivo:
    info = json.load(arquivo)
    login = info["login"]
    senha = info["senha"]
 
dsn = cx_Oracle.makedsn(
    host = 'oracle.fiap.com.br',
    port = 1521,
    sid = 'ORCL'
)
 
conn = cx_Oracle.connect(
    user = login,
    password = senha,
    dsn = dsn
)
 
cursor = conn.cursor()
 
 
cursor.execute("INSERT INTO PERSONS VALUES ('1', 'Vitor', 'Gomes')")
cursor.execute("SELECT * FROM PERSONS")
rows = cursor.fetchall()
print(rows)
 
 
cursor.close()
conn.close()
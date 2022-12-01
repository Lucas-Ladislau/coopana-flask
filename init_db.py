import psycopg2
import psycopg2.extras
import os
#Versão de conexão docker
DB_HOST = os.environ['DB_HOST']
DB_NAME = os.environ['DB_DBNAME']
DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASS']

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASS, host=DB_HOST)

#Gera o banco ao iniciar
try:
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    sql = open('./Coopana_PG.sql', 'r').read()
    sql_comandos = sql.split(
        "----------------------------------------------------------------")
    for i in range(0, len(sql_comandos)-1, 2):
        try:
            cur.execute(sql_comandos[i])
        except:
            print("Erro ao executar comando: ", sql_comandos[i])
except:
    print("Banco já esta criado")

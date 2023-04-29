import mysql.connector

# Conectando o banco de dadps
config = {
    'user': 'admin',
    'password': 'aulanoiteFaculdade',
    'host': 'dbaula.cddn3xpihyde.us-east-1.rds.amazonaws.com',
    'database': 'aula'
}

#Estabelecer a conexão com o bancos de dados 
try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")

#Criando um objeto curspr para executar aa consultas do SQL
cursor = conn.cursor()

#Inserindo o estado na tabela
sql = "SELECT * FROM estado"
cursor.execute(sql)

#Obter o resultado da consulta
result = cursor.fetchall()
print(result)
result

#Imprimindo os resultados 
for linhas in result:
    print(linhas)
    
#Fechar a conexão e o curso 
conn.close()
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

#Solicitando a entrega ao usuario
busca = input("Digite o nome que deseja buscar: ")

#Executando a onsulta com LIKE
sql = "SELECT * FROM estado WHERE nome LIKE %s"
val = ("%" + busca +"%",)
cursor.execute(sql, val)

#obtendo os resultados
results = cursor.fetchall()

#iterando os resultados 
for result in results:
    print(result)
    
#Fechar a conexão e o curso 
conn.close()
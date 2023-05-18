import mysql.connector

# Definir as informações de conexão
config = {
  'user': 'usuarioremoto',
  'password': 'minhasenha',
  'host': '44.197.184.141',
  'database': 'aula'
}

# Estabelecer a conexão com o banco de dados
try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")
# Fechar a conexão


def conectar():
    mybd = mysql.connector.connect(
        host = '44.197.184.141',
        user = 'usuarioremoto',
        password = 'minhasenha',
        database = 'aula'
    )
    return mybd
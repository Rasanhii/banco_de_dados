from conexao import conectar

def listar(conn, cursor):
    # Abrir uma conexão com o vvanco de dados
    conn = conectar()
    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()
    # executar a consulta SQL para listar os registros
    cursor.execute("SELECT * FROM estado")
    #obter os resultados
    resultados = cursor.fetchall()
    # imprimir os resultados
    for resultado in resultados:
        print(resultado)
    # fechar a conexão e o cursor
    cursor.close()
    conn.close()
    
    
def inserir(codigo, nome):
    # Abrir uma conexão com o vvanco de dados
    conn = conectar()
    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()
    # executar a consulta SQL para listar os registros
    sql = 'INSERT INTO estado (codigo,nome) VALUES (%s, %s)'
    val = (codigo, nome)
    cursor.execute(sql, val)
    #commit da transação
    conn.commit()
    #imprimir mensagens de sucesso
    print('Registro inserido com sucesso.')
    #imprimir a conexão e o cursor
    cursor.close()
    conn.close()
    
    
def atualizar(codigo, novo_nome):
    # Abrir uma conexão com o vvanco de dados
    conn = conectar()
    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()
    # executar a consulta SQL para listar os registros
    sql = 'UPDATE estado SET nome = %s WHERE codigo = %s'
    val = (novo_nome, codigo)
    cursor.execute(sql, val)
    #commit da transação
    conn.commit()
    
    if cursor.rowcount == 0:
        print('Nenhum registro atualizado.')
    else:
        print('Registro atalizado com sucessor')
    #fechar a conexão e o cursor
    cursor.close()
    conn.close()
    
    
def deletar(codigo):
    # Abrir uma conexão com o vvanco de dados
    conn = conectar()
    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()
    # executar a consulta SQL para listar os registros
    sql = 'DELETE FROM estado WHERE codigo = %s'
    val = (codigo,)
    cursor.execute(sql, val)
    #commit da transação
    conn.commit()
    
    if cursor.rowcount == 0:
        print('Nenhum registro deletado.')
    else:
        print('Registro deletado com sucessor')
    #fechar a conexão e o cursor
    cursor.close()
    conn.close()

conn = conectar()

cursor = conn.cursor()

while True:
  # Mostra as opções de operação
  print("O que você deseja fazer?")
  print("1 - Listar estados")
  print("2 - Inserir novo estado")
  print("3 - Atualizar um estado")
  print("4 - Deletar um estado")
  print("0 - Sair")
  
  opcao = int(input("Digite o número da opção desejada: "))

  if opcao == 1:
    # Listar estados
    listar(conn, cursor)
  
  elif opcao == 2:
    # Inserir novo estado
    codigo = int(input("Digite o código do novo estado: "))
    nome = input("Digite o nome do novo estado: ")
    inserir(codigo, nome)

  elif opcao == 3:
    # Atualizar um estado
    codigo = int(input("Digite o código do estado que deseja atualizar: "))
    nome = input("Digite o novo nome do estado: ")
    atualizar(codigo, nome)

  elif opcao == 4:
    # Deletar um estado
    codigo = int(input("Digite o código do estado que deseja deletar: "))
    deletar(codigo)

  elif opcao == 0:
    # Sair do programa
    break

  else:
    print("Opção inválida. Digite novamente.")
    
# Fechar a conexão e o cursor
cursor.close()
conn.close()
from conexao import conectar

# chama a função conectar
conn = conectar()

# criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()

# solicitando a entrada do usuário
busca = input('Digite o nome do estado que deseja excluir: ')

# executando a consulta com LIKE para verificar se o registro
sql = 'SELECT * FROM estado WHERE nome LIKE %s'
val = ('%' + busca + '%',)
cursor.execute(sql, val)

# obtendo o resultado
result = cursor.fetchone()

if result:
    codigo = result[0]
    nome = result[1]
    
    confirmacao = input(f'Tem certeza que deseja deletar "{nome}"? (s/n): ')
    if confirmacao.lower() == 's':
        sql = 'DELETE FROM estado WHERE codigo = %s'
        val = (codigo,)
        cursor.execute(sql, val)
        conn.commit()
        print(f'O estado {nome} foi deletado com sucesso')
    else:
        print('Operação cancelado pelo usuário.')

# se o resultado for nulo, o registro não existe
else:
    print('Não foi encontrado nenhum estado com o nome informado')
    
# fechar o cursor
conn.close()
# Importa a conexão Singleton do banco de dados
from banco import conexao_singleton as cs

# Obtém uma instância de conexão com o banco de dados
conexao = cs.Conexao().get_conexao()

# Função para listar todas as produções do banco de dados
def listar_todos() -> list:
    # SQL para selecionar todos os registros da tabela "producoes"
    sql: str = "SELECT * FROM producoes"

    # Utiliza a conexão para abrir um cursor e executar o SQL
    with conexao.cursor() as cursor:
        cursor.execute(sql)
        # Obtém todos os resultados da consulta
        resultado = cursor.fetchall()

        # Cria uma lista das colunas retornadas pela consulta
        colunas = [desc[0] for desc in cursor.description]
        # Mapeia os resultados em dicionários com chave-valor
        dados = [dict(zip(colunas, linha)) for linha in resultado]

        return dados

# Função para listar as produções de um pesquisador específico
def listar_por_pesquisador(pesquisadores_id: str) -> list:
    # SQL para selecionar as produções de um pesquisador pelo seu ID
    sql: str = "SELECT * FROM producoes WHERE pesquisadores_id = %s"

    with conexao.cursor() as cursor:
        cursor.execute(sql, (pesquisadores_id,))
        resultado = cursor.fetchall()

        colunas = [desc[0] for desc in cursor.description]
        dados = [dict(zip(colunas, linha)) for linha in resultado]

        return dados

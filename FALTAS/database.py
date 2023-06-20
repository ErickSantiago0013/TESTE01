import sqlite3

# Conecta-se ao banco de dados (ou cria um novo se não existir)
conn = sqlite3.connect('cadastros.db')
cursor = conn.cursor()

# Cria a tabela "cadastro" se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cadastro (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT,
        nome TEXT,
        cargo TEXT,
        loja TEXT,
        salario REAL
    )
''')

# Fecha a conexão com o banco de dados
conn.close()

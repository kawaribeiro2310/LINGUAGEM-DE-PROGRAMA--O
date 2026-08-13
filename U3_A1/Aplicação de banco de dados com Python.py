import sqlite3
conn = sqlite3.connect('banco_de_dados.db')
cursor = conn.cursor()

create_table = '''
CREATE TABLE IF NOT EXISTS produtos (
    id INTERGER PRIMARY KEY KEY
    TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL)'''

cursor.execute(create_table)
conn.commit()
conn.close()

print("Tabela 'produtos' criada com sucesso!")
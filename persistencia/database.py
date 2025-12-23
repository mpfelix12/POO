import sqlite3

class Database:
    def __init__(self, nome_db='banco.db'):
        self.conexao = sqlite3.connect(nome_db)
        self.conexao.execute("PRAGMA foreign_keys = ON")
        self.criar_tabelas()

    def criar_tabelas(self):
        cursor = self.conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS canal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS quadro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            canal_id INTEGER,
            FOREIGN KEY(canal_id) REFERENCES canal(id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS video (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            url TEXT NOT NULL,
            assistido INTEGER,
            quadro_id INTEGER,
            FOREIGN KEY(quadro_id) REFERENCES quadro(id)
        )
        """)

        self.conexao.commit()

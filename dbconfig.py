import sqlite3

class DBHandler:
    def __init__(self):
        self.db = sqlite3.connect('contatos')
        self.cursor = self.db.cursor()

    def cria_tabelas(self):
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS contatos (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL); 
                            CREATE TABLE IF NOT EXISTS telefones (
                                id_telefone INTEGER PRIMARY KEY AUTOINCREMENT,
                                ddd TEXT NOT NULL,
                                telefone TEXT NOT NULL,
                                id_contatos INTEGER,
                                FOREIGN KEY (id_contatos) REFERENCES contatos(id) ON DELETE CASCADE); 
                            CREATE TABLE IF NOT EXISTS emails (
                                id_email INTEGER PRIMARY KEY AUTOINCREMENT,
                                email TEXT NOT NULL,
                                id_contatos INTEGER,
                                FOREIGN KEY (id_contatos) REFERENCES contatos(id) ON DELETE CASCADE);""");
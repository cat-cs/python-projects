import sqlite3
from tabulate import tabulate as tb

class DBHandler:
    def __init__(self):
        self.db = sqlite3.connect('contatos.db')
        self.cursor = self.db.cursor()
        self.cria_tabelas()

    def cria_tabelas(self):
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS Contatos (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL)""")
                            
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS Telefones (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                ddd TEXT NOT NULL,
                                numero TEXT NOT NULL,
                                id_contato INTEGER,
                                FOREIGN KEY (id_contato) REFERENCES Contatos(id) ON DELETE CASCADE)""")
                            
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS Emails (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                email TEXT NOT NULL,
                                id_contato INTEGER,
                                FOREIGN KEY (id_contato) REFERENCES Contatos(id) ON DELETE CASCADE);""")
        self.db.commit()


    def inserir_item (self, tabela, colunas, valor):
        itens = ", ".join(["?"] * len(valor))
        query= f'INSERT INTO {tabela} ({colunas}) VALUES ({itens})'
        self.cursor.execute(query, valor)
        self.db.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido



    def exibe_item(self, tabela, campos, id):
        query = f'SELECT {campos} FROM {tabela} WHERE id = ?'
        self.cursor.execute(query, (id,))
        if campos.lower() == "nome":
            item = self.cursor.fetchone()
            return item[0].upper()
        else:
            item = self.cursor.fetchall()
            return item

    def exibe_db(self):
        query = 'SELECT Contatos.id, Contatos.Nome, GROUP_CONCAT(DISTINCT Emails.email SEPARATOR "; ") AS Emails, GROUP_CONCAT(DISTINCT CONCAT("(", Telefones.ddd,") " ,Telefones.numero) SEPARATOR "; ") AS Telefones FROM Contatos LEFT JOIN Telefones ON Contatos.id = Telefones.id_contato INNER JOIN Emails ON Contatos.id = Emails.id_contato GROUP BY Contatos.id, Contatos.Nome;'
        self.cursor.execute(query)
        resultado = self.cursor.fetchall()
        print(tb(resultado, headers=["ID", "Nome", "Emails", "Telefones"], tablefmt="grid"))



    def deleta_item(self, tabela, id):
        query = f'DELETE FROM {tabela} WHERE id = ?'
        self.cursor.execute(query, (id,))
        self.db.commit();



    def atualiza_contato(self, tabela, campo, novo_item, id):
        query = f'UPDATE {tabela} SET {campo}=? WHERE id = ?'
        self.cursor.execute(query, (novo_item, id))
        self.db.commit();
    
    def close_connection(self):
        self.db.close()

    @property
    def colunas_str(self): 
        return {"colunas_telefone": "ddd, numero, id_contato", 
                "colunas_email": "email, id_contato",
                "campos_telefone_update": "ddd= ?, numero= ?"}
    
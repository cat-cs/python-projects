import sqlite3

class DBHandler:
    def __init__(self):
        self.db = sqlite3.connect('contatos.db')
        self.cursor = self.db.cursor()
        self.cria_tabelas()

    def cria_tabelas(self):
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS Contatos (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL); 
                            
                            CREATE TABLE IF NOT EXISTS Telefones (
                                id_telefone INTEGER PRIMARY KEY AUTOINCREMENT,
                                ddd TEXT NOT NULL,
                                numero TEXT NOT NULL,
                                id_contato INTEGER,
                                FOREIGN KEY (id_contato) REFERENCES Contatos(id) ON DELETE CASCADE); 
                            
                            CREATE TABLE IF NOT EXISTS Emails (
                                id_email INTEGER PRIMARY KEY AUTOINCREMENT,
                                email TEXT NOT NULL,
                                id_contato INTEGER,
                                FOREIGN KEY (id_contato) REFERENCES Contatos(id) ON DELETE CASCADE);""");
        self.cursor.commit()


    def inserir_item (self, tabela, colunas, valor):
        itens = ", ".join(["?"] * len(valor))
        query= f'INSERT INTO {tabela} ({colunas}) VALUES ({itens})'
        self.cursor.execute(query, valor)
        self.cursor.commit();
        return self.cursor.lastrowid;


    def exibe_item(self, tabela, campos, id):
        query = f'SELECT {campos} FROM {tabela} WHERE id = ?'
        self.cursor.execute(query, id)
        item = self.cursor.fetchone()
        if isinstance(item[0], str):
             return item[0].upper();
        else: 
            return item;

    def ler_DB(self):
        query = 'SELECT Contatos.id, Contatos.Nome, GROUP_CONCAT(DISTINCT Emails.email SEPARATOR "; ") AS Emails, GROUP_CONCAT(DISTINCT CONCAT("(", Telefones.ddd,") " ,Telefones.numero) SEPARATOR "; ") AS Telefones FROM Contatos LEFT JOIN Telefones ON Contatos.id = Telefones.id_contato INNER JOIN Emails ON Contatos.id = Emails.id_contato GROUP BY Contatos.id, Contatos.Nome;'
        self.cursor.execute(query)
        resultado = self.cursor.fetchall()
        return resultado;

    ### def buscar_contato(self, id):

    def deleta_contato(self, id):
        query = f'DELETE FROM contatos WHERE id = ?'
        self.cursor.execute(query, id)
        self.cursor.commit();

    def atualiza_contato(self, tabela, campo, novo_item, id):
        query = f'UPDATE {tabela} SET {campo}=? WHERE id = ?'
        self.cursor.execute(query, (novo_item, id))
        self.cursor.commit();
    
    """def atualiza_telefone_contato(self, ddd, numero, id):
        query = f'UPDATE telefones SET ddd= ?, numero= ? WHERE id_telefone = ?'
        self.cursor.execute(query, (ddd, numero, id))
        self.cursor.commit();"""

    @property
    def colunas_str(self): 
        return {"colunas_telefone": "ddd, numero, id_contato", 
                "colunas_email": "email, id_contato",
                "campos_telefone_update": "ddd= ?, numero= ?"}
    
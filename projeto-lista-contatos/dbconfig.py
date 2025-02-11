import sqlite3

class DBHandler:
    def __init__(self):
        self.db = sqlite3.connect('contatos')
        self.cursor = self.db.cursor()

    def cria_tabelas(self):
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS Contatos (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL); 
                            
                            CREATE TABLE IF NOT EXISTS Telefones (
                                id_telefone INTEGER PRIMARY KEY AUTOINCREMENT,
                                ddd TEXT NOT NULL,
                                numero TEXT NOT NULL,
                                id_contato INTEGER,
                                FOREIGN KEY (id_contatos) REFERENCES Contatos(id) ON DELETE CASCADE); 
                            
                            CREATE TABLE IF NOT EXISTS Emails (
                                id_email INTEGER PRIMARY KEY AUTOINCREMENT,
                                email TEXT NOT NULL,
                                id_contato INTEGER,
                                FOREIGN KEY (id_contatos) REFERENCES Contatos(id) ON DELETE CASCADE);""");
        self.cursor.commit()

##verificar se funcionar com Telefones
    def inserir_item (self, tabela, colunas, valor):
        itens = ", ".join(["?"] * len(valor))
        query= f'INSERT INTO {tabela} ({colunas}) VALUES ({itens})'
        self.cursor.execute(query, (valor))
        self.cursor.commit();


    def exibe_item(self, tabela, campos, id):
        query = f'SELECT {campos} FROM {tabela} WHERE id = ?'
        self.cursor.execute(query, (id,))
        item = self.cursor.fetchone()
        if isinstance(item, str):
             return item[0].upper();
        else: 
            return item;

    def ler_DB(self):
        query = 'SELECT contatos.id, contatos.Nome, GROUP_CONCAT(DISTINCT emails.Email SEPARATOR "; ") AS Emails, GROUP_CONCAT(DISTINCT CONCAT("(", telefones.DDD,") " ,telefones.Telefone) SEPARATOR "; ") AS Telefones FROM contatos LEFT JOIN telefones ON contatos.id = telefones.id_contatos INNER JOIN emails ON contatos.id = emails.id_contatos GROUP BY contatos.id, contatos.Nome;'
        self.cursor.execute(query)
        resultado = self.cursor.fetchall()
        return resultado;

    ### def buscar_contato(self, id):

    def deleta_contato(self, id):
        query = f'DELETE FROM contatos WHERE id = ?'
        self.cursor.execute(query, (id))
        self.cursor.commit();

    def atualiza_contato(self, tabela, campo, novo_item, id):
        query = f'UPDATE {tabela} SET {campo}=? WHERE id = ?'
        self.cursor.execute(query, (novo_item, id))
        self.cursor.commit();
    
    def atualiza_telefone_contato(self, ddd, numero, id):
        query = f'UPDATE telefones SET ddd= ?, numero= ? WHERE id_telefone = ?'
        self.cursor.execute(query, (ddd, numero, id))
        self.cursor.commit();

    @staticmethod
    def colunas_em_str(): 
        colunas_str = {"colunas_telefone": "DDD, numero, id_contato", 
                   "colunas_email": "Email, id_contatos"}
        return colunas_str
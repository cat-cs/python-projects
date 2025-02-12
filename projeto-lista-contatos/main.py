"""

##IMPRIME LISTA
contatos_all= ler_DB()
print(contatos_all(resultado, headers=["ID", "Nome", "Emails", "Telefones"], tablefmt="grid"))


###DELETAR
id_delete = int (input("Digite ID para selecionar um contato -> "))
    nomeExcluido = exibe_item(Contatos, nome, id_delete)
    verifica = input (f"Deseja excluir o contato de {nomeExcluido}? Digite SIM/NAO\n -> ")
    if verifica.upper() == "SIM":
        deleta_contato(id_delete)
        print("___Contato excluído com sucesso!___ \n")
    elif verifica.upper() == "NAO":
        print("Retornando ao menu...");
    else:
        print("Opção Inválida. Digite SIM ou NAO");

###Cria contato
contato = Contato.cria_contato()
inserir_item (Contatos, nome, contato.nome):
contato.id = cursor.lastrowid

(tabela, campos, valor):
    inserir_item(Telefones, colunas_str[campos_telefone], (contato.id)
    inserir_email (Emails, colunas_str[campos_email], (contato.email, contato.id))

'''
    def salvar_contato():
        contato.id = self.db.inserir_item("Contatos", "nome", (contato.nome,))

        for email in contato.emails:
            self.db.inserir_item("Emails", db.colunas_str[campos_email], (email, contato.id))

        for telefone in contato.telefones:
            self.db.inserir_item("Telefones", db.colunas_str[campos_telefone], (telefone["ddd"], telefone["numero"], contato.id))

'''


    print("___Contato adicionado a lista com sucesso!___");

"""
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
contato = cria_contato()
inserir_item (Contatos, nome, contato.nome):
contato.id = cursor.lastrowid

(tabela, campos, valor):
    inserir_item(Telefones, colunas_str[campos_telefone], contato.id)
    inserir_email (Emails, contato.email, contato.id)

    print("___Contato adicionado a lista com sucesso!___");

"""
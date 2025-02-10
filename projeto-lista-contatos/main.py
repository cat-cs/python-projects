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




"""
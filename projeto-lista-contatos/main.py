from contato import Contato
from dbconfig import DBHandler

def menu():
    print("1. Criar contato")
    print("2. Exibir contatos")
    print("3. Atualizar contato")
    print("4. Deletar contato")
    print("5. Sair")
    return input("Escolha uma opção: ")

def criar_contato(db):
    contato = Contato(nome="")
    contato.cria_contato(db)


def exibir_contatos(db):
    db.exibe_db()

def atualizar_contato(db):
    id_contato = int(input("Digite o ID do contato a ser atualizado: "))
    campo = input("Digite o campo a ser atualizado: 1.Nome | 2.Email | 3.Telefone ")
    


    novo_valor = input(f"Digite o novo valor para {campo}: ")
    db.atualiza_item(campo, novo_valor, id_contato)

def deletar_contato(db):
    id_contato = int(input("Digite o ID do contato a ser deletado: "))
    nome_excluido = db.exibe_item("Contatos", "nome", id_contato)
    verifica = input(f"Deseja excluir o contato de {nome_excluido}? Digite SIM/NAO: ")
    if verifica.upper() == "SIM":
        db.deleta_item("Contatos", id_contato)
        print("___Contato excluído com sucesso!___")
    elif verifica.upper() == "NAO":
        print("Retornando ao menu...")
    else:
        print("Opção Inválida. Digite SIM ou NAO")

if __name__ == "__main__":
    db = DBHandler()
    while True:
        opcao = menu()
        if opcao == "1":
            criar_contato(db)
        elif opcao == "2":
            exibir_contatos(db)
        elif opcao == "3":
            atualizar_contato(db)
        elif opcao == "4":
            deletar_contato(db)
        elif opcao == "5":
            db.close_connection()
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


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
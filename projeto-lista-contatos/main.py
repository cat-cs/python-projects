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
    id_contato = input("Digite o ID do contato a ser atualizado: ")
    opcao = int(input("Escolha o campo a ser atualizado: 1.Nome | 2.Email | 3.Telefone "))

    if opcao == 1: 
            tabela = "Contatos"
            coluna = "nome"
            
    elif opcao == 2:
            tabela = "Emails"
            coluna = "email"
            
    elif opcao == 3:
            tabela = "Telefones"
            coluna = "numero"
            
    else:
         print("Opção inválida. Tente novamente.")

    novo_valor = input(f"Digite o novo valor para {coluna.upper()}: ")
    db.atualiza_item(tabela, coluna, novo_valor, id_contato)


def deletar_contato(db):
    id_contato = int(input("Digite o ID do contato a ser deletado: "))
    nome_excluido = db.exibe_item("Contatos", "nome", id_contato)
    verifica = input(f"Deseja excluir o contato de {nome_excluido}? Digite SIM/NAO: ")
    if verifica.upper() == "SIM":
        db.deleta_item("Contatos", id_contato)
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


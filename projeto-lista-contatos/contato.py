from dataclasses import dataclass, field
from typing import List, Dict, Optional
from dbconfig import DBHandler as db


@dataclass
class Contato:
    id: Optional[int] = None
    nome: str
    emails: List[str] = field(default_factory=list)
    telefones: List[Dict[str, str]] = field(default_factory=list)


    def cria_contato(self):
        print("___Adcione as informações de contato___")
        
        while True:
            self.nome = input("Nome: ")
            while True:
                email = Contato.input_email()
                self.emails.append(email)
                if input("Deseja adicionar outro email? (S/N): ").strip().upper() != "S":
                    break
                
            while True:
                telefone = Contato.input_telefone()
                self.telefones.append(telefone)
                if input("Deseja adicionar outro telefone? (S/N): ").strip().upper() != 'S':
                    break
                
            if input(
                Contato.salvar_contato(self)
            ).strip().upper() == 'S':
                self.salvar_contato()
                break
    

    def salvar_contato(self):
        self.id = db.inserir_item("Contatos", "nome", (self.nome))

        for email in self.emails:
            db.inserir_item("Emails", db.colunas_str['colunas_email'], (email, self.id))

        for telefone in self.telefones:
            db.inserir_item("Telefones", db.colunas_str['colunas_telefone'], (telefone["ddd"], telefone["numero"], self.id))


    @staticmethod    
    def input_email():
        email = input("Email: ")
        return email

    @staticmethod
    def input_telefone():
        ddd = input("DDD: ")
        numero = input("Telefone: ")
        Contato.valida_telefone(ddd, numero)
        return {"ddd": ddd, "numero": numero}


    @staticmethod
    def valida_telefone(ddd, numero):
        if len(ddd) != 2 or not ddd.isdigit():
            raise ValueError("DDD deve ter 2 dígitos.")
        if len(numero) != 9 or not numero.isdigit():
            raise ValueError("Número deve ter 9 dígitos.")
        
    
        
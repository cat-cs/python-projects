from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Contato:
    id: int = None
    nome: str
    emails: list[str] = field(default_factory=list)
    telefones: list[Dict[str, str]] = field(default_factory=list)


    def cria_contato(self):
        print("___Adcione as informações de contato___")
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
        
    
        
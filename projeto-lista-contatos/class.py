from dataclasses import dataclass, field
from typing import List

@dataclass
class Telefone:
    id_contato: int = None
    ddd: str
    numero: str

@dataclass
class Email:
    id_contato: int = None
    endereco: str

@dataclass
class Contato:
    id: int = None
    nome: str
    emails: list[Email] = field(default_factory=list)
    telefones: list[Telefone] = field(default_factory=list)

    ###def create
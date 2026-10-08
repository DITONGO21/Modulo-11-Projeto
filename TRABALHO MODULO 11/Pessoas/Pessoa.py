from abc import ABC, abstractmethod

class Pessoas(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        if not novo_nome:
            raise ValueError("O nome nao pode estar vazio.")
        self._nome = novo_nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            raise ValueError("A idade nao pode ser negativa")
        self._idade = nova_idade

    @abstractmethod
    def mostrar_informações(self) -> None:
        pass
    

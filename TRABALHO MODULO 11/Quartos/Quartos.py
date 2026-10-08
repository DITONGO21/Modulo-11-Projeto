from abc import ABC, abstractmethod

class Quartos(ABC):
    def __init__(self, numero, tipo, preco_diaria):
        self.numero = numero
        self.tipo = tipo
        self.preco_diaria = preco_diaria
        self._ocupado = False

    @property
    def ocupado(self):
        return self._ocupado

    @property
    def preco_diaria(self):
        return self._preco_diaria

    @preco_diaria.setter
    def preco_diaria(self, novo_preco):
        if novo_preco < 0:
            raise ValueError("O preco nao pode ser negativo.")
        self._preco_diaria = novo_preco

    def ocupar(self):
        self._ocupado = True

    def libertar(self):
        self._ocupado = False

    @abstractmethod
    def calcular_preco(self, dias) -> float:
        pass

    def mostrar_informações(self):
        if self.ocupado:
            estado = "Ocupado"
        else:
            estado = "Livre"
        print(f"Quarto {self.numero} | Tipo: {self.tipo} | Preco: {self.preco_diaria} | Estado: {estado}")

class QuartoSimples(Quartos):
    def __init__(self, numero, preco_diaria=50):
        super().__init__(numero, "Simples", preco_diaria)

    def calcular_preco(self, dias):
        return self.preco_diaria * dias

class QuartoLuxo(Quartos):
    def __init__(self, numero, preco_diaria=120):
        super().__init__(numero, "Luxo", preco_diaria)

    def calcular_preco(self, dias):
        return round(self.preco_diaria * dias * 1.15, 2)

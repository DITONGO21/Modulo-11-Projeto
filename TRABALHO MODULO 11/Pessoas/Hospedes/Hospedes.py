from Pessoas.Pessoa import Pessoas

class Hospede(Pessoas):
    def __init__(self, nome, idade, dias_estadia, quarto=None):
        super().__init__(nome, idade)
        self.__dias_estadia = dias_estadia
        self.__quarto = None

        if idade < 18:
            print("Erro, não pode ser menor")
        
        if quarto is not None:
            self.quarto = quarto

    @property
    def quarto(self):
        return self.__quarto

    @quarto.setter
    def quarto(self, novo_quarto):
        if novo_quarto.ocupado:
            raise ValueError("O quarto nao esta livre.")
        self.__quarto = novo_quarto
        novo_quarto.ocupar()

    def atribuir_quarto(self, quarto):
        self.quarto = quarto

    def calcular_conta(self):
        if self.__quarto is None:
            return 0
        return self.__quarto.calcular_preco(self.__dias_estadia)

    def mostrar_informações(self):
        if self.__quarto is None:
            print(f"Nome: {self.nome} | Idade: {self.idade} | Quarto: Sem quarto")
        else:
            print(f"Nome: {self.nome} | Idade: {self.idade} | Quarto: {self.__quarto.numero}")

    def checkout(self):
        if self.__quarto is not None:
            self.__quarto.libertar()
            self.__quarto = None
        print(f"{self.nome} fez check-out. Ate breve!")

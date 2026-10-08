from Pessoas.Funcionarios.Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome: str, id_func: int, idade: int, salario: int):
        super().__init__(nome, id_func, idade, salario)
        self.__bonus = salario * 0.1

    def mostrar_informações(self):
        print(f"Nome do Gerente: {self.nome} | Idade: {self.idade} | Salario + Bonus: {self._salario + self.__bonus}")

    def gerar_relatorio(self, funcionarios):
        for funcionario in funcionarios:
            funcionario.mostrar_informações()

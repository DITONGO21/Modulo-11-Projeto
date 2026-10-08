from Pessoas.Pessoa import Pessoas

class Funcionario(Pessoas):
    def __init__(self, nome: str, id_func: int, idade: int, salario: int):
        super().__init__(nome, idade)
        self._id_func = id_func
        self._salario = salario # atributo protegido

    def mostrar_informações(self):
        print(f"Nome: {self.nome} | ID: {self._id_func} | Idade: {self.idade} | Salario: {self._salario}")

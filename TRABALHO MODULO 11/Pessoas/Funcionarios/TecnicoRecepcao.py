from Pessoas.Funcionarios.Recepcionista import Recepcionista
from Pessoas.Funcionarios.TecnicoManutencao import TecnicoManutencao

class TecnicoRecepcao(Recepcionista, TecnicoManutencao):

    def __init__(self, nome, id_func, idade, salario, turno, especialidade):
        Recepcionista.__init__(self, nome, id_func, idade, salario, turno)
        TecnicoManutencao.__init__(self, nome, id_func, idade, salario, especialidade)

    def mostrar_informações(self):
        print(
            f"Nome: {self.nome} | "
            f"ID: {self._id_func} | "
            f"Idade: {self.idade} | "
            f"Salário: {self._salario} | "
            f"Turno: {self.turno} | "
            f"Especialidade: {self.especialidade}"
        )

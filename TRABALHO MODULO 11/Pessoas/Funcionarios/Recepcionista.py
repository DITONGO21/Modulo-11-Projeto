from Pessoas.Funcionarios.Funcionario import Funcionario

class Recepcionista(Funcionario):
    def __init__(self, nome, id_func, idade, salario, turno):
        Funcionario.__init__(self, nome, id_func, idade, salario)
        self.turno = turno

    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, novo_turno):
        if novo_turno not in ("manhã", "tarde", "noite"):
            raise ValueError("Turno invalido (manhã, tarde, noite).")
        self._turno = novo_turno

    def mostrar_informações(self):
        print(f"Nome: {self.nome} | ID: {self._id_func} | Idade: {self.idade} | Salario: {self._salario} | Turno: {self.turno}")

    def registrar_hospede(self, hospede, lista_hospedes):
        lista_hospedes.append(hospede)
        print(f"Hospede {hospede.nome} registado com sucesso.")

    def listar_hospedes(self, lista_hospedes):
        for hospede in lista_hospedes:
            hospede.mostrar_informações()

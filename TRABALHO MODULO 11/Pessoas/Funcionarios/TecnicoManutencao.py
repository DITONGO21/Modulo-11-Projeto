from Pessoas.Funcionarios.Funcionario import Funcionario


class TecnicoManutencao(Funcionario):

    def __init__(self, nome, id_func, idade, salario, especialidade):
        super().__init__(nome, id_func, idade, salario)
        self._especialidade = especialidade
        self._reparos = []

    @property
    def especialidade(self):
        return self._especialidade

    def mostrar_informações(self):
        print(
            f"Nome: {self.nome} | "
            f"ID: {self._id_func} | "
            f"Idade: {self.idade} | "
            f"Salário: {self._salario} | "
            f"Especialidade: {self.especialidade}"
        )

    def registrar_reparo(self, descricao):
        self._reparos.append(descricao)
        print(f"Reparo registado: {descricao}")

    def listar_reparos(self):
        if not self._reparos:
            print("Não existem reparos registados.")
            return

        print(f"\nReparos realizados por {self.nome}:")
        for reparo in self._reparos:
            print(f"- {reparo}")
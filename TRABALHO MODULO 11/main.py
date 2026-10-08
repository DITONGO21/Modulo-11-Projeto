from Pessoas.Hospedes.Hospedes import Hospede
from Pessoas.Funcionarios.Gerente import Gerente
from Pessoas.Funcionarios.Recepcionista import Recepcionista
from Pessoas.Funcionarios.TecnicoManutencao import TecnicoManutencao
from Pessoas.Funcionarios.TecnicoRecepcao import TecnicoRecepcao
from Quartos.Quartos import QuartoSimples, QuartoLuxo

lista_quartos = [QuartoSimples(101), QuartoSimples(102), QuartoLuxo(201), QuartoLuxo(202)]
lista_hospedes = []

gerente = Gerente("Carlos Sousa", 1, 45, 2500)
recepcionista = Recepcionista("Ana Silva", 2, 30, 1000, "manhã")
tecnico_manutencao = TecnicoManutencao("Rui Costa", 3, 35, 1100, "Eletricidade")
tecnico_recepcao = TecnicoRecepcao("Marta Reis", 4, 28, 1200, "tarde", "Canalização")
lista_funcionarios = [gerente, recepcionista, tecnico_manutencao, tecnico_recepcao]

opcao = 0

while opcao != 3:
    print("\n=== MENU ===")
    print("1 - Entrar como hóspede")
    print("2 - Entrar como Funcionário")
    print("3 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida! Digite um número.")
        continue

    if opcao == 1:
        opcao_hospede = 0

        while opcao_hospede != 4:
            print("\n=== MENU HÓSPEDE ===")
            print("1 - Fazer reserva")
            print("2 - Ver conta")
            print("3 - Fazer check-out")
            print("4 - Voltar")

            try:
                opcao_hospede = int(input("Escolha uma opção: "))
            except ValueError:
                print("Opção inválida!")
                continue

            if opcao_hospede == 1:
                nome = input("Nome: ")
                try:
                    idade = int(input("Idade: "))
                    if idade < 18:
                        print("Erro: Apenas pessoas com 18 anos ou mais podem fazer check-in.")
                        continue
                    dias_estadia = int(input("Dias de estadia: "))
                except ValueError:
                    print("Por favor introduza números válidos para a idade/dias.")
                    continue

                print("\nQuartos livres:")
                quartos_livres = [q for q in lista_quartos if not q.ocupado]
                if not quartos_livres:
                    print("Não há quartos livres no momento.")
                    continue

                for quarto in quartos_livres:
                    quarto.mostrar_informações()

                try:
                    numero = int(input("Número do quarto: "))
                except ValueError:
                    print("Número do quarto inválido!")
                    continue

                quarto_selecionado = None
                for quarto in quartos_livres:
                    if quarto.numero == numero:
                        quarto_selecionado = quarto
                        break

                if quarto_selecionado:
                    try:
                        hospede = Hospede(nome, idade, dias_estadia)
                        hospede.atribuir_quarto(quarto_selecionado)
                        recepcionista.registrar_hospede(hospede, lista_hospedes)
                    except ValueError as e:
                        print(f"Erro ao registar hóspede: {e}")
                else:
                    print("Quarto inexistente ou ocupado!")

            elif opcao_hospede in (2, 3):
                nome = input("Nome do hóspede: ")
                hospede_encontrado = None
                
                for h in lista_hospedes:
                    if h.nome == nome:
                        hospede_encontrado = h
                        break

                if hospede_encontrado:
                    if opcao_hospede == 2:
                        print(f"Total da estadia(€): {hospede_encontrado.calcular_conta()}")
                    else:
                        hospede_encontrado.checkout()
                        lista_hospedes.remove(hospede_encontrado)
                else:
                    print("Hóspede não encontrado!")

            elif opcao_hospede == 4:
                print("A voltar...")
            else:
                print("Opção inválida! Tente novamente.")

    elif opcao == 2:
        opcao_funcionario = 0

        while opcao_funcionario != 6:
            print("\n=== MENU FUNCIONÁRIO ===")
            print("1 - Listar hóspedes (Recepcionista)")
            print("2 - Listar quartos (Recepcionista)")
            print("3 - Gerar relatório de funcionários (Gerente)")
            print("4 - Registar reparo (Técnico de Manutenção)")
            print("5 - Ações do Técnico de Receção (Herança Múltipla)")
            print("6 - Voltar")

            try:
                opcao_funcionario = int(input("Escolha uma opção: "))
            except ValueError:
                print("Opção inválida!")
                continue

            if opcao_funcionario == 1:
                recepcionista.listar_hospedes(lista_hospedes)
            elif opcao_funcionario == 2:
                for quarto in lista_quartos:
                    quarto.mostrar_informações()
            elif opcao_funcionario == 3:
                gerente.gerar_relatorio(lista_funcionarios)
            elif opcao_funcionario == 4:
                tecnico_manutencao.registrar_reparo(input("Descrição do reparo: "))
            elif opcao_funcionario == 5:
                print("\n[Técnico de Receção - Herança Múltipla]")
                print("Como herdo de ambas as classes, posso:")
                print("-> Registar um reparo (Manutenção)")
                tecnico_recepcao.registrar_reparo(input("Descrição do reparo: "))
                print("\nE também listar hóspedes (Recepcionista)")
                tecnico_recepcao.listar_hospedes(lista_hospedes)
            elif opcao_funcionario == 6:
                print("A voltar...")
            else:
                print("Opção inválida! Tente novamente.")

    elif opcao == 3:
        print("A encerrar o sistema. Até breve!")
    else:
        print("Opção inválida! Tente novamente.")
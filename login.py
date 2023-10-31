import funcoes

def cadastrarFuncionario():
    while True:
        print("-" * 59)
        print('-' * 9 + "RH360 - CADASTRO FUNCIONÁRIOS - PETPALLET" + '-' * 9)
        print("-" * 59)
        print("\n1- Cadastrar\n2- Pesquisar\n3- Listar todos os Funcionários\n4- Voltar")
        escolha1 = input("Escolha uma opção: ")

        if escolha1 == "1":
            nome = input("Digite o nome do funcionário: ")
            cargo = input("Digite o cargo: ")
            salario = input("Digite o salário: ")
            email = input("Digite o e-mail: ")
            funcoes.bancoDados(nome, cargo, salario, email)
            pass

        elif escolha1 == "2":
            nomePesquisa = input("Digite o nome do funcionário que deseja pesquisar: ")
            funcoes.pesquisarPessoa(nomePesquisa)

        elif escolha1 == "3":
            funcoes.listaPessoa()

        elif escolha1 == "4":
            principal()

def cadastrarFiliais():
    while True:
        print("-" * 59)
        print('-' * 9 + "RH360 - CADASTRO DE FILIAIS - PETPALLET" + '-' * 9)
        print("-" * 59)
        print("\n1- Cadastrar\n2- Pesquisar\n3- Listar todas as filiais\n4- Voltar")
        escolha1 = input("Escolha uma opção: ")

        if escolha1 == "1":
            cidade = input("Digite o nome da cidade: ")
            endereco = input("Digite o endereco: ")
            telefone = input("Digite o telefone: ")
            numero = input("Digite o numero da filial: ")
            funcoes.bancoDadosFiliais(cidade, endereco, telefone, numero)
            pass

        elif escolha1 == "2":
            cidadePesquisa = input("Digite o nome da cidade que deseja pesquisar: ")
            funcoes.bancoFiliais(cidadePesquisa)

        elif escolha1 == "3":
            funcoes.listaFilial()

        elif escolha1 == "4":
            principal()

def CargosSalarios():
    while True:
        print("-" * 59)
        print('-' * 9 + "RH360 - CARGOS E SALÁRIOS - PETPALLET" + '-' * 9)
        print("-" * 59)
        print("\n1- Pesquisar por código\n2- Listar todos os cargos\n3- Voltar")
        escolha1 = input("Escolha uma opção: ")

        if escolha1 == "1":
            codigoT = input("Digite o código que deseja pesquisar: ")
            funcoes.pesquisarTabela(codigoT)

        elif escolha1 == "2":
            funcoes.listaTabela()

        elif escolha1 == "3":
            principal()

def principal():
    while True:
        print("-" * 59)
        print('-' * 20 + "Sistema de cadastro" + '-' * 20)
        print("-" * 59)
        print("\nSeja bem-vindo!\n1- Cadastrar Funcionários\n2- Cadastrar Filiais\n3- Cargos e Salários\n4- Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrarFuncionario()

        if escolha == "2":
            cadastrarFiliais()

        if escolha == "3":
            CargosSalarios()

        if escolha == "4":
            break

principal()


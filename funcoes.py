
def criarlogin():
    nome = input("Crie o nome de login: ")
    return nome

def criarCargo():
    cargo = input("Qual o cargo: ")
    return cargo

def criarSalario():
    salario = int(input("Qual o salario: "))
    return salario
def criarEmail():
    email = input("Qual o email: ")
    return email

def bancoDados(nome, cargo, salario, email):
    with open("bancoFuncionarios.txt", "a") as arquivo:
        arquivo.write(f"Nome do funcionário: {nome}\n")
        arquivo.write(f"Cargo: {cargo}\n")
        arquivo.write(f"Salario: {salario}\n")
        arquivo.write(f"Email: {email}\n")
        arquivo.write("-------------------------\n")
    print("Sucesso! Funcionario salvo com sucesso")

def pesquisarPessoa(nome):
    with open("bancoFuncionarios.txt", "r") as arquivo:
        conteudo = arquivo.read()
        if f"Nome do funcionário: {nome}" in conteudo:
            print("-------------------------")
            inicio = conteudo.find(f"Nome do funcionário: {nome}")
            fim = conteudo.find("-------------------------", inicio)
            if inicio != -1 and fim != -1:
                dados = conteudo[inicio:fim + len("-------------------------")]
                print("Dados do funcionário:\n")
                print(dados)
            else:
                print(f"funcionário com nome '{nome}' não encontrada.")
        else:
            print(f"funcionário com nome '{nome}' não encontrada.")

def listaPessoa():
    with open("bancoFuncionarios.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print("-------------------------")
        print(conteudo)

#funcoes filiais
def bancoDadosFiliais(cidade, endereco, telefone, numero):
    with open("bancoFiliais.txt", "a") as arquivo:
        arquivo.write(f"Nome da cidade: {cidade}\n")
        arquivo.write(f"Endereco: {endereco}\n")
        arquivo.write(f"Telefone: {telefone}\n")
        arquivo.write(f"Numero: {numero}\n")
        arquivo.write("-------------------------\n")
    print("Sucesso! Filial salva com sucesso")

def bancoFiliais(cidade):
    with open("bancoFiliais.txt", "r") as arquivo:
        conteudo = arquivo.read()
        if f"Nome da cidade: {cidade}" in conteudo:
            print("-------------------------")
            inicio = conteudo.find(f"Nome da cidade: {cidade}")
            fim = conteudo.find("-------------------------", inicio)
            if inicio != -1 and fim != -1:
                dados = conteudo[inicio:fim + len("-------------------------")]
                print("Dados da filial:\n")
                print(dados)
            else:
                print(f"Nome da cidade '{cidade}' não encontrada.")
        else:
            print(f"Nome da cidade '{cidade}' não encontrada.")

def listaFilial():
    with open("bancoFiliais.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print("-------------------------")
        print(conteudo)

#Tabela
def pesquisarTabela(codigoT):
    with open("table.txt", "r") as arquivo:
        conteudo = arquivo.read()
        if f"Codigo: {codigoT}" in conteudo:
            print("-------------------------")
            inicio = conteudo.find(f"Codigo: {codigoT}")
            fim = conteudo.find("-------------------------", inicio)
            if inicio != -1 and fim != -1:
                dados = conteudo[inicio:fim + len("-------------------------")]
                print("Dados do codigo:\n")
                print(dados)
            else:
                print(f"Codigo '{codigoT}' não foi encontrada.")
        else:
            print(f"Codigo '{codigoT}' não foi encontrada.")

def listaTabela():
    with open("table.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print("-------------------------")
        print(conteudo)


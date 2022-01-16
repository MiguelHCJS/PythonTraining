def perguntar():
    resposta = input("Digite a letra, correspondente: <I>Inserir usuário, <P> Pesquisar, <E> Excluir ou <L> Listar:").upper()
    return resposta


def inserir(dicionario):
    dicionario[input('Nome de usuário: ').upper()] = [input('Nome: '), input("Data de nascimento: "), input("Setor: ")]


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista is not None:
        print('Nome: ' + lista[0])
        print('Data de nascimento: ' + lista[1])
        print('Setor: ' + lista[2])


def excluir(dicionario, chave):
    if dicionario.get(chave) is not None:
        del dicionario[chave]
    print("Exclusão realizada")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print('Usuário.......')
        print('Login: ', chave)
        print('Dados: ', valor)

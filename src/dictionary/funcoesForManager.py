def perguntar():
    resposta = input("Digite a letra, correspondente: <I>Inserir usuário, <P> pesquisar ou <E> Excluir:").upper()
    return resposta


def inserir(dicionario):
    dicionario[input('Nome de usuário: ').upper()] = [input('Nome: '), input("Data de nascimento: "), input("Setor: ")]


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista is not None:
        print('Nome: ' + lista[0])
        print('Data de nascimento: ' + lista[1])
        print('Setor: ' + lista[2])

def chamarMenu():
    escolha = int(input('Digite: <1> Para registrar ativo, <2> Para persistir em arquivo, <3> Para exibir ativos armazenados: '))
    return escolha


def registrar(dicionario):
    resp = 's'
    while resp == 's':
        dicionario[input('Digite o número patrimonial: ')] = [
            input('Digite a data da última atualização: '),
            input('Digite a descrição: '),
            input('Digite o departamento: ')]
        resp = input('Digite <s> para inserir outro patrimônio.')


def persistir(dicionario):
    with open('inventario.csv', 'a') as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + "\n")
    return 'Persistido com sucesso!'


def exibir():
    with open('inventario.csv', 'r') as inv:
        lines = inv.readlines()
    return lines

from funcoesForManager import *

usuarios = {}

opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    elif opcao == "P":
        pesquisar(usuarios, input('Qual usuário quer pesquisar? ').upper())
        print('--------\n')
    elif opcao == "E":
        excluir(usuarios, input('Quer excluir qual usuário? ').upper())
        print('--------\n')
    elif opcao == "L":
        listar(usuarios)
    opcao = perguntar()

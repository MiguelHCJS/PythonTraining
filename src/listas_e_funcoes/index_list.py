nome = []
pais = []

resposta = 's'

while resposta == 's':
    nome.append(input('Nome: '))
    pais.append(input('Pais de nascimento: '))
    resposta = input('Mais inclusões? ')

for indice in range(0, len(nome)):
    print("Indices por inclusão: ", (indice + 1))
    print(f'Nome {nome}')
    print(f'Pais {pais}')

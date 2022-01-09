inventario = []
resposta = input('Inserir equipamento? ')
while resposta == 's':
    equipamento = [
        input('Equipamento: '),
        float(input('Valor: ')),
        int(input('Número de série: ')),
        input('Departamento: ')
    ]
    inventario.append(equipamento)
    resposta = input('Inserir mais um equipamento? ')

for elemento in inventario:
    print('Nome........: ', elemento[0])
    print('Valor.......: ', elemento[1])
    print('Série.......: ', elemento[2])
    print('Departamento: ', elemento[3])
    print('---------------------------')

buscar = input('Digite o nome do equipamento para buscá-lo: ')
for elemente in inventario:
    if buscar == elemento[0]:
        print('Valor.......: ', elemento[1])
        print('Série.......: ', elemento[2])
        print('Departamento: ', elemento[3])

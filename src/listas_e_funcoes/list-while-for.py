deposito = []
resposta = 'S'
while resposta == 'S':
    deposito.append(input('Equipamento: '))
    deposito.append(input('Valor unitário: '))
    deposito.append(input('Número de série: '))
    deposito.append(input('Departamento: '))
    resposta = input('Mas algum item?').upper()

for elemente in deposito:
    print(elemente)

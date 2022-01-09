nome = []
admissao = []
cargo = []

resposta = 'S'

while resposta == 'S':
    nome.append(input('Nome: '))
    admissao.append(input('Data da admissão: '))
    cargo.append(input('Cargo: '))
    resposta = input('Mais uma inclusão? ').upper()

for n_funciorario in nome:
    print(f'O funcionário {nome}, foi admitido em {admissao} e com a função {cargo}.')

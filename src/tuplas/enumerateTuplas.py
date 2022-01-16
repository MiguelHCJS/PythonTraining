usuarios = {}
resp = "s"
emails = []
while resp == "s":
    emails.append(input('Digite um e-mail: ').lower())
    resp = input('Digite "s" para inserir mais um e-mail: ').lower()
    print("-------")

tupla = list(enumerate(emails))
for chave in range(0, len(tupla)):
    print('E-mail: ', tupla[chave][1])
    usuarios[tupla[chave]] = [input('Nome: '), input('Nível: ')]

for chave, dado in usuarios.items():
    print("--------------------")
    print('Usuário.: ', chave[0])
    print('E-mail..: ', chave[1])
    print('Nome....: ', dado[0])
    print('Nível...: ', dado[1])

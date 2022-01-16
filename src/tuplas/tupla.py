ips = {}

resp = "S"

while resp == "S":
    ips[(input('Digite os dois primeiros octetos: '),
        input('Digite os dois últimos octetos: '))] = input('Nome da maquina: ')
    resp = input('Digite "S" para inserir outra máquina: ').upper()

print("'Exibindo ip's: ")
for ip in ips.keys():
    print(ip[0] + '.' + ip[1])

print('Máquinas com o mesmo endereço: ')
pesquisar = input('Digite os dois últimos octetos: ')
for ip, nome in ips.items():
    print('-- Máquinas no mesmo endereço(redes diferentes) --')
    if(ip[1] == pesquisar):
        print(nome)

print('Máquinas na mesma rede: ')
rede = input('Digite os dois primeiros octetos: ')
for ip, nome in ips.items():
    print('-- Máquinas na mesma rede(diferente endereços -- ')
    if(ip[0] == rede):
        print(nome)

resposta = input('Logar no sistema? "S" ou "N"')

while resposta == "S":
    nivel = input('Você vai logar como "ADM", "USER", "GUEST"?').upper()
    if nivel == "ADM" or "USER" or "GUEST":
        genero = input('Genero de preferencia? "M" ou "F"?').upper()
        if nivel == "ADM":
            if genero == "M":
                print('Olá administrador!')
            else:
                print('Olá administradora!')
        elif nivel == "USER":
            if genero == "M":
                print('Olá usuário!')
            else:
                print('Olá usuária!')
        elif nivel == "GUEST":
            print('Olá visitante!')
        else:
            print('Olá desconhecido!')
    else:
        print('Obrigado!')

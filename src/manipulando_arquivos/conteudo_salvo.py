""" with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.read()
"""

with open('/home/migueltenorio/Documentos/PythonTraining/src/manipulando_arquivos/teste.txt', 'w') as arquivo:
    arquivo.write('Tudo certo!\r')

with open('/home/migueltenorio/Documentos/PythonTraining/src/manipulando_arquivos/teste.txt', 'a') as arquivo:
    arquivo.write('Uhum!')

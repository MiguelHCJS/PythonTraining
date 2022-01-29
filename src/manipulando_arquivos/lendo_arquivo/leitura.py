with open('/home/migueltenorio/Documentos/PythonTraining/src/manipulando_arquivos/lendo_arquivo/teste.txt', 'w') as arquivo:
    arquivo.write('Texto para teste.')

with open('/home/migueltenorio/Documentos/PythonTraining/src/manipulando_arquivos/lendo_arquivo/teste.txt', 'r') as arquivo:
    conteudo = arquivo.read()

print(f'Tipo de arquivo {type(conteudo)}')
print(f'Conteúdodo do arquivo: {conteudo}')

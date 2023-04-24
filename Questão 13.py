#Crie um dicionário vazio. Peça para o usuário digitar as chaves e os valores desse dicionário. 
#Em seguida, verifique se a chave 'profissão' está presente no dicionário.

print('Digite uma chave e um valor: ')
dicionário = {}

chave = input('Chave: ')
valor = input('Valor: ')
dicionário[chave] = valor
  
print(dicionário)

if 'profissão' or 'Profissão' in dicionário:
    print('A chave - Profissão - está presente no dicionário')
else:
    print('A chave - Profissão - não está presente no dicionário')
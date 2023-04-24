#Crie um dicionário vazio. Peça para o usuário digitar uma chave e um valor e 
#adicione esses dados ao dicionário. Em seguida, peça para o usuário adicionar mais uma chave 
#e um valor e adicione esses dados a(o dicionário também.

print('Digite uma chave e um valor: ')
dicionário = {}

chave = input('Chave: ')
valor = input('Valor: ')
dicionário[chave] = valor
  
print(dicionário)

print('Digite mais uma chave e mais um valor: ')

chave2 = input('Chave: ')
valor2 = input('Valor: ')
dicionário[chave2] = valor2

print('Dicionário com os adicionais: ', dicionário)


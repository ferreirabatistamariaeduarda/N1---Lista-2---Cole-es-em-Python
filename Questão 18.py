#Crie um dicionário vazio. Peça para o usuário digitar as chaves e os valores desse dicionário. 
#Em seguida, adicione uma nova chave e valor ao dicionário, onde a chave é 'cidade' e o valor é a 
#cidade em que o usuário nasceu.

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

cidade = input("Digite a cidade de nascimento: ")
dicionário["cidade"] = cidade


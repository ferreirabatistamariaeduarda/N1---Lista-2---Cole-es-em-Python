#Crie uma lista vazia e peça para o usuário digitar 10 números. 
#Em seguida, adicione esses números à lista utilizando um loop for.

print('Digite 10 números: ')
lista = []

for i in range(10):
    numeros = input(f'Digite o {i+1}ª número: ')
    lista.append(numeros)
    
print(lista)
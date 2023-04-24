#Peça para o usuário digitar 5 números e crie uma tupla com esses números. 
#Em seguida, retorne o primeiro elemento da tupla.

print('Digite 5 números: ')
tupla = ()

for i in range(5):
    numeros = input(f'Digite o {i+1}ª numero: ')
    tupla += (numeros,) #concatenação
    
print(tupla)

primeiroElemento = tupla[0]

print('Retornando ao 1ª elemento da tupla: ', primeiroElemento)

#Peça para o usuário digitar 5 números e crie um conjunto com esses números. 
#Em seguida, verifique quantos elementos estão no conjunto.

conjunto = set()

print('Digite 5 números')

for i in range(5):
    numeros = input(f'Digite o {i+1}ª numero: ')
    conjunto.add(numeros)
    
quant = len(conjunto)
    
print(conjunto)
print(f'A quantidade de elementos nesse conjunto é {quant}')
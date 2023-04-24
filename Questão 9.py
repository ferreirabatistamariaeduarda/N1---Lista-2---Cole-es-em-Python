#Peça para o usuário digitar 10 números e crie um conjunto com esses números. 
#Em seguida, remova todos os números pares do conjunto.

conjunto = set()

print('Digite 10 números')

for i in range(10):
    numeros = int(input(f'Digite o {i+1}ª numero: '))
    conjunto.add(numeros) #concatenação
    
print(conjunto)

numPares = set()

for j in conjunto:
    if j % 2 == 0:
      numPares.add(j)
    
conjunto -= numPares
    
print('Conjunto sem os números pares: ', conjunto)

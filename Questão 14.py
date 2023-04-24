#Peça para o usuário digitar 5 números e crie um conjunto com esses números. 
#Em seguida, verifique se o número 3 está presente no conjunto.

conjunto = set()

print('Digite 5 números')

for i in range(5):
    numeros = input(f'Digite o {i+1}ª numero: ')
    conjunto.add(numeros) 
    
print(conjunto)

if 3 in conjunto:
    print('O número - 3 - está presente no dicionário')
else:
    print('O número - 3 - não está presente no dicionário')
#Peça para o usuário digitar 5 números e crie um conjunto com esses números. 
#Em seguida, peça para o usuário escolher um dos números e removê-lo do conjunto.

conjunto = set()

print('Digite 5 números')

for i in range(5):
    numeros = input(f'Digite o {i+1}ª numero: ')
    conjunto.add(numeros) #concatenação
    
print(conjunto)

print('Agora escola um dos números digitados para ser removido')

remover = input('Número a ser removido: ')

if remover in conjunto:
    conjunto.remove(remover)
    
print(conjunto)

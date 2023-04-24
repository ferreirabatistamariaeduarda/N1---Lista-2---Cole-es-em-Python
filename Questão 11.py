#Crie uma lista vazia e peça para o usuário digitar 10 números. 
#Em seguida, retorne os elementos de índice par da lista.

print('Digite 10 números')
lista = []

for i in range(10):
    num = int(input(f'Digite o {i+1}ª número: '))
    lista.append(num)
    
print(lista)

par = []
for num in lista:
    if num % 2 == 0:
        par.append(num)
    
print(par)
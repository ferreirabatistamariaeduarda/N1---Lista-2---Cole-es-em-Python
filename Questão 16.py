#Peça para o usuário digitar 10 números e crie uma lista com esses números. 
#Em seguida, multiplique cada elemento da lista por 2 e crie uma nova lista com esses valores.

print('Digite 10 números')
lista = []

for i in range(10):
    num = int(input(f'Digite o {i+1}ª número: '))
    lista.append(num)
    
print(lista)

mult = []
for j in lista:
    mult.append(j * 2)
    
print(mult)
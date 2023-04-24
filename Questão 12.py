#Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. 
#Em seguida, verifique se o nome 'Maria' está presente na tupla.
print('Digite 3 nomes')
tupla = ()

for i in range(3):
    nomes = str(input(f'Digite o {i+1}ª nome: '))
    tupla += (nomes,) #concatenação
    
print(tupla)

if 'maria' or 'Maria' in tupla:
    print('o nome - Maria - está presente na tupla')
else:
    print('o nome - Maria - não está presente na tupla')
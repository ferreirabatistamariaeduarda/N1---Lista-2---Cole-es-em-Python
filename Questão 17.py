#Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. 
#Em seguida, verifique quantas vezes o nome 'Maria' aparece na tupla.
tupla = ()

for i in range(3):
    nums = input(f'Digite o {i+1}ª nome: ')
    tupla += (nums,) #concatenação
    
print(tupla)

quantTupla = tupla.count('Maria' or 'maria')

print(f'O nome Maria aparece {quantTupla} vez(es) na tupla')
#Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. 
#Em seguida, peça para o usuário escolher um dos nomes e substituir 
#esse nome por outro nome que ele também deve digitar.

tupla = ()

for i in range(3):
    nomes = input(f'Digite o {i+1}ª nome: ')
    tupla += (nomes,) #concatenação
    
print(tupla)
print('Substitua um nome acima')

nomeAntigo = input('Digite o nome que deseja substituir: ')

if nomeAntigo in tupla:
    nomeNovo = input('Digite um novo nome: ')
    
lista = list(tupla) #mudar para lista, para acessar a tupla

subs = lista.index(nomeAntigo)
lista[subs] = nomeNovo

tupla = tuple(lista) #mudando a lista para tupla

print('os nomes atualizados são: ', lista)
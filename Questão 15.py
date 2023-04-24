#Crie um grafo vazio. Peça para o usuário digitar os vértices e as arestas desse grafo. 
#O usuário deve informar os pares de vértices que formam cada aresta. 
#Em seguida, verifique se a aresta ('A', 'C') está presente no grafo.

grafo = {}

quantVertices = int(input('Digite a quantidade de vértices: '))

for i in range(quantVertices):
    vertices = input(f'Digite o nome do vértice {i+1}: ')
    grafo[vertices] = []

quantArestas = int(input('Digite a quantidade de arestas: '))

for j in range(quantArestas):
    a, b = input(f'Digite os pares de vértices que formam a aresta {j+1}: ').split()
    grafo[a].append(b)
    grafo[b].append(a)

print(grafo)

if ('A, C') in grafo:
    print('Esta aresta está presente no grafo')
else:
    print('Esta aresta não está presente no grafo')

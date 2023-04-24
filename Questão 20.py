#Crie um grafo vazio. Peça para o usuário digitar os vértices e as arestas desse grafo. 
#O usuário deve informar os pares de vértices que formam cada aresta. Em seguida, mostre o grafo.


# Criando um grafo vazio
grafo = {}

# Adicionando vértices ao grafo
grafo['A'] = []
grafo['B'] = []
grafo['C'] = []
grafo['D'] = []

# Adicionando arestas ao grafo
grafo['A'].append('B')
grafo['B'].append('A')
grafo['B'].append('C')
grafo['C'].append('B')
grafo['C'].append('D')
grafo['D'].append('C')

# Exibindo o grafo
print(grafo)

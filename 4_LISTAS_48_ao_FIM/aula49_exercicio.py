"""
for in com listas
"""
"""
exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
lista.insert(2, 'Gabriel')
i = 0

for nome in lista:
    print(i, nome)
    i += 1
"""
## OU ##
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
"""
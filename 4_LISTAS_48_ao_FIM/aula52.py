"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# DESSA FORMA, EU CONSUMO OS ITENS, ENTÃO EM UM SEGUNDO FOR NÃO FUNCIONARIA
# lista_enumerada = enumerate(lista)

# for item in lista_enumerada:
#     print(item)
"""
# PARA RESOLVER, USA-SE O ENUMERATE DIRETAMENTE NA LISTA AO INVÉS DE CRIAR UMA OUTRA VARIÁVEL 

for item in enumerate(lista):
    print(item)
for item in enumerate(lista):
    print(item)
for item in enumerate(lista):
    print(item)
for item in enumerate(lista):
    print(item)  

#posso usar diversas vezes que irá imprimir todas
"""
# POSSO TAMBÉM FAZER DO ENUMERATE UMA LISTA OU TUPLA
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
# lista_enumerada = list(enumerate(lista))       #(lista, start=10), começa a enumerar do numero 10#
# print(lista_enumerada)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

## O PYTHON FAZ ISSO AUTOMATICAMENTE, MOSTRA O INDICE E O NOME PARA CADA ITEM DO FOR:

for indice, nome in enumerate(lista):
    print(indice, nome)
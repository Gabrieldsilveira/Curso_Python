"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append - Adiciona um item ao final 
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, Ler, alterar, apagar = lista[i] (CRUD)
"""
"""
Cuidados com dados mutáveis
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# lista = [123, True, 'Luiz Otávio', 1.2, []]
# print(lista)
# lista[2] = 'Gabriel'
# print(lista)

# lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

# lista.append(50)
# lista.pop()
# lista.append(60)
# lista.append(70)
# ultimo_valor = lista.pop() #pop retorna um valor e posso fazer o que quiser com ele
# print(ultimo_valor)
# print(lista)

# lista.append('Luiz')
# nome = lista.pop()
# lista.append (1233)
# del lista[-1]
# lista.insert(0, 5)
# #       indice, item à adicionar
# print(lista)

# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b
# lista_a.extend(lista_b) # extend mexe diretamente na lista que está atuando
# # lista_d = lista_a.extend(lista_b) --- retornaria nulo
# print(lista_a)
# print(lista_c)


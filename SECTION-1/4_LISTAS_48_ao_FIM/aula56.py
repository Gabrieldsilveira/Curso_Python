"""
Lista de Listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0        1       2       3-0  1   2   3   4
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)],  # 2
]

# print(salas) # [['Maria', 'Helena'], ['Elaine'], ['Luiz', 'João', 'Eduarda']]
# print(salas[1]) # ['Elaine']
# print(salas[1][0]) # Elaine -- Acesso o VALOR do índice 1 e não O índice
# # Para buscar o VALOR 'Helena':
# print(salas[0][1])
# # Para buscar o valor 20 do índice 2 de salas:
# print(salas[2][3][2])

for sala in salas:
    for item in sala:
        print(item)
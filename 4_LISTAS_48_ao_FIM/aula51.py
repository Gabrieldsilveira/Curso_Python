"""
tipo tupla - uma lista imutável
UMA FORMA DE CRIAR É NÃO COLOCAR OS COLCHETES
ou
ENTRE PARÊNTESES
"""

"""
nomes = 'Maria', 'Helena', 'Luiz'
# nomes[1] = 'Outro' #tupla não aceita ser mudada
print(nomes)
"""
nomes = ['Maria', 'Helena', 'Luiz']
# MUDAR UMA LISTA PARA UMA TUPLE
nomes = tuple(nomes)
print(type(nomes))
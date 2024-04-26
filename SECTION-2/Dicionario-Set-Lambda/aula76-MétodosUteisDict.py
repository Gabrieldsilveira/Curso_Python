# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - apaga um item com a chave especificada (del)
# popitem - apaga o último item adicionado
# update - atualiza um dicionário com outro


pessoa = {
    'nome': 'Gabriel',
    'idade': 26
}

print(len(pessoa), '-- len')
print()

# keys retorna as chaves - podemos converter ex list(pessoa.keys())
print(pessoa.keys(), '-- keys')
print()

# values retorna os valores das chaves - pessoa.values()
for p in pessoa.values():
    print(p, '-- values')
print()

# items retorna (chave, valor)
# print(pessoa.items())
for p, v in pessoa.items():
    print(p, v, '-- items')
print()

# setdefault eu passo um valor para um chave inexistente
pessoa.setdefault('sobrenome', 'Dutra')
print(pessoa['sobrenome'], '-- setdefault')
print()


# copy no caso do dicts, o valor de igual indica que a segunda variável é representado pelo mesmo dict, ou list
# então o = não copia, usamos copy (É COPIA RASA POIS ELE NÃO ENTRA NOS SUBINDICES), muda apenas itens mutáveis dentro do dict,
# uma list dentro do dict não seria alterada de maneira individual
# PARA UMA COPIA MAIS PROFUNDA, d2 = copy.deepcopy(d1)

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

d2 = d1.copy()

d2['c1'] = 1000
d2['l1'][1] = 99999 # irá alterar d1 e d2
print(d1)
print(d2)

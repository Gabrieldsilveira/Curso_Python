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

p1 = {
    'nome': 'Gabriel',
    'sobrenome': 'Dutra'
}

# o pop ele deleta um item especificado, mas também retorna o valor dele:
# nome = p1.pop('nome')
# print(nome)
# print(p1)

## ##

# popitem deleta a ultima chave do dict ao inves de uma especificada
# ultimaChave = p1.popitem()
# print(ultimaChave)
# print(p1)

## ##

# update pode alterar chaves, criar novas, tudo ao mesmo tempo:
# p1.update({
#     'nome': 'novo valor',
#     'idade': 26
# })
 
# print(p1)

## OU ##

# p1.update(nome='novo valor', idade=26)
# print(p1)

## OU ##

tupla = (('nome', 'novo valor'), ('idade', 26))
p1.update(tupla)
print(p1)
# serviria com list também
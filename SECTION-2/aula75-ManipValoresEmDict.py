# MANIPULANDO CHAVES E VALORES EM DICIONÁRIOS

pessoa = {}

##
##

# Posso criar uma chave dentro do dict assim:
# pessoa['nome'] = 'Gabriel Dutra'
# print(pessoa)
# print()

# Podemos alterar uma variavel do dict, e também criar dessa forma:

chave = 'nome'

pessoa[chave] = 'Gabriel D'
pessoa['sobrenome'] = 'da Silveira'
# print(pessoa['nome'])
# print(pessoa)

# Podemos também deletar um item do dict:

del pessoa['sobrenome']
print(pessoa) # o sobrenome não existe mais
print(pessoa['nome'])

# Para evitar uma exceção ao chamar um valor que não exista usamos .get() -- RETORNA None SE NÃO EXISTIR

# print(pessoa.get('sobrenome'))  ---- None

if pessoa.get('sobrenome') is None:
    print('Não existe "sobrenome"')
else:
    print(pessoa['sobrenome'])



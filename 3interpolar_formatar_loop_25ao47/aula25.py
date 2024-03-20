"""
INTERPOLAÇÃO BÁSICA DE STRINGS %

%s - string
%d e %i - int
%f - float
%x e %X - hexadecimal (abcdef0123456789)
"""
nome = 'Gabriel'
preco = 1000.9567
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('o hexadecimal de %d é %X' % (15, 15))


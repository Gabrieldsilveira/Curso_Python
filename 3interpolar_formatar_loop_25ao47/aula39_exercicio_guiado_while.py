# nome = input('Digite seu nome: ')
# qnt_letras = len(nome)
# contador = 0

# while contador < qnt_letras:
#     print(nome[contador],end='*')
#     contador += 1

"""
OU
"""

nome = input('Digite seu nome: ')  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)



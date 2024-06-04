import string

"""
TEMPO DE EXECUÇÃO LOGARÍTMICO O(Log n)
"""

## LISTA COM LETRAS DO ALFABETO
alfabeto = list(string.ascii_lowercase)

## SENTENÇA PARA CRIPTOGRAFAR
sentença = 'A marlene e muito mandrioninha'

## SUBSTRING A SER CRIADA
sentençaCriptografada = ''

## SISTEMA COM PESQUISA BINARIA:
def pesquisaBinaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio + 3
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

for i in sentença.lower():
    if i == ' ':
        sentençaCriptografada += ' '
        continue
    index = pesquisaBinaria(alfabeto, i)
    sentençaCriptografada += alfabeto[index]

print(sentençaCriptografada)








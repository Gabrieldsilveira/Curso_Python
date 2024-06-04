import string

"""
TEMPO DE EXECUÇÃO LINEAR O(n)
"""


## LISTA COM LETRAS DO ALFABETO
alfabeto = list(string.ascii_lowercase)

## SENTENÇA PARA CRIPTOGRAFAR
sentença = 'a marlene e muito mandrioninha'

## SUBSTRING A SER CRIADA
sentençaCriptografada = ''
letraTrocada = ''

## SISTEMA USANDO FOR
for i in sentença.lower(): 
    if i == ' ':
        sentençaCriptografada += i   
        continue 
    for letra in alfabeto:            
        if i == letra:
            index = alfabeto.index(i)
            letraTrocada = alfabeto[index + 4]
            sentençaCriptografada += letraTrocada
            break

print(sentençaCriptografada)
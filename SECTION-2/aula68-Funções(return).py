"""
Retorno de valores das funções (return)
"""

# def soma(x, y):
#     # return ACABA a função, antes disso posso colocar o que quiser
#     return x + y # se eu NÃO colocar esse return, a função retorna o VALOR nulo

# soma1 = soma(2, 2) # retorna valor 4, e não nulo
# soma2 = soma(3, 3) # retorna valor 6, e não nulo
# print(soma1 + soma2) # retorna valor soma1 + soma2 (4 + 6 = 10)

def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y # ELSE NÃO É NECESSÁRIO, POIS SÓ PODE 1 RETURN POR FUNÇÃO
                 # SE O IF FOR EXECUTADO, ELE RETORNARÁ AQUELE VALOR.


# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))
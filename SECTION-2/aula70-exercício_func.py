# EXERCÍCIOS COM FUNÇÕES

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variavel

def calculo(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

var1 = calculo(1, 2, 3, 4, 5)
print(var1)

# Crie uma função fala se um numero e par ou impar.
# Retorne se o número é par ou ímpar.

n = int(input('Digite um número: '))

def par_impar(n):
    var = ''
    if n % 2 == 0:
        return 'par'
    return 'impar'

var = par_impar(n)
print(var)
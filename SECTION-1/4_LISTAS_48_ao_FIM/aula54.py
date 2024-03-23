"""
imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3) # printa 0.7999999...
# O python, e outras linguagens não consegue mostrar exatamente o numero como ele é
"""
PODEMOS USAR round(numero, n. casas decimais), apesar de definir 2 ou mais casas decimais,
ele irá mostrar apenas o número arredondado, sem os zeros.
"""
print(round(numero_3, 2)) # printa 0.8

"""
OUTRA MANEIRA - import decimal
numero_1 = decimal.Decimal('0.1')
.
.
.
PARA QUANDO PRECISAR DE MUUITA PRECISÃO NO CÓDIGO
"""



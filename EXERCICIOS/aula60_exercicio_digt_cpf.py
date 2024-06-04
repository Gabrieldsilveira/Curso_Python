"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
cpf = input('Digite o cpf: ')
lista = []
for i in cpf:
    if i == '.' or i == '-':
        continue
    lista.append(i)
    
    
lista.pop(-1)
lista.pop(-1)


soma_nums_1 = 0
contador = 10
for item in lista:
    soma_nums_1 += int(item) * contador
    contador -= 1


digito_1 = (soma_nums_1 * 10) % 11
digito_1 = 0 if digito_1 > 9 else digito_1

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
"""
lista.append(digito_1)

soma_nums_2 = 0
contador2 = 11
for item in lista:
    soma_nums_2 += int(item) * contador2
    contador2 -= 1


digito_2 = (soma_nums_2 * 10) % 11
digito_2 = 0 if digito_2 > 9 else digito_2
   
print(f'Primeiro digito: {digito_1}')
print(f'Segundo digito: {digito_2}')

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um número: ')

if entrada.isdigit():  
    int_entrada = int(entrada)
    par_impar = int_entrada % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'
        
    print(f'O número {int_entrada} é {par_impar_texto}')
else:
    print('O que você digitou não é um número inteiro')

    
    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hora = input('Digite o horário de agora: ')
# int_hora = int(hora)

# if int_hora >= 0 and int_hora <= 11:
#     print('Bom dia!')

# if int_hora >= 12 and int_hora <= 17:
#     print('Boa tarde!')

# if int_hora >= 18 and int_hora <= 23:
#     print('Boa noite!')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# nome_usuario = input('Digite seu nome: ')
# quantidade_letras = len(nome_usuario)
 
# if quantidade_letras <= 4:
#     print('Seu nome é curto')
    
# if quantidade_letras >= 5 and quantidade_letras <= 6:
#     print('Seu nome é normal')
        
# if quantidade_letras > 6:
#     print('Seu nome é muito grande')
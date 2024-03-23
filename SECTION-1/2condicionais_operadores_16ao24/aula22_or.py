# OPERADORES LÓGICOS
# and (e) or(ou) not(não)

# or - Qualquer expressão como verdadeira, toda expressão será verdadeira.
# São considerados Falsy: 0  0.0  ''  False e também *none* que é um não número.

# entrada = input('[E]ntrar [S]air: ')
# senha = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha == senha_permitida: 
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
# print(True or False) -#irá retornar o primeiro valor verdadeiro, então:
senha = input('Senha: ') or 'Senha incorreta'
print(senha)
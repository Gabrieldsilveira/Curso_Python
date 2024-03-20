# OPERADORES LÓGICOS
# and (e) or(ou) not(não)

# and - Todas as condições precisam ser verdadeiras.
# Se alguma for falsa, toda a expressão sera falsa.
# são considerados falsy:
# 0     0.0     ''      False
# Há também o tipo *none* que é usado para representar um não valor.

entrada = input('[E]ntrar [S]air: ')
senha = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha == senha_permitida: 
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
print(True and False and True)





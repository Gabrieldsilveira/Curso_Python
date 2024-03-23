# Coletar dados do usuário com a função **input** (TORNA TUDO STR)

# nome = input('Qaul o seu nome?:')
# print(f'O seu nome é {nome=}') #ou {nome} apenas

# a função input ira transformar o numero em str, então a soma irá concatenar
# numero_1 = input('Digite um número: ')
# numero_2 = input('Digite outro número: ')

# print(f'A soma dos dois números é: {numero_1 + numero_2}')

# Podemos transformar a str em int, mas é prudente fazer isso em uma variável que fique após a checagem dos números (VEREMOS DEPOIS):

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos dois números é: {int_numero_1 + int_numero_2}')


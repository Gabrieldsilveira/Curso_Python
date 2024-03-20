# FORMATAÇÃO DE STRINGS - f-strings

# Gabriel Dutra tem 1.85 de altura, pesa 78 quilos e seu IMC é 22.79
# nome = 'Gabriel Dutra'
# altura = 1.85
# peso = 78 
# imc = peso / altura ** 2

# print(nome, 'tem', altura, 'de altura,',) 
# print('pesa', peso, 'quilos e seu IMC é',)
# print('imc')


# para formatar, atribuimos a linha que queremos a uma variável como uma string, ex:
# linha_1 = 'nome tem altura de altura'

# Então adicionamos o comando f antes, para indicar que queremos usar as variáveis na string:
# linha_1 = f'nome tem altura de altura'

# Depois colchetes nas variáveis:
# linha_1 = f'{nome} tem {altura} de {altura}'

nome = 'Gabriel Dutra'
altura = 1.85
peso = 78 
imc = peso / altura ** 2

# Podemos ainda indicar quantas casas decimais queremos depois da vírgula em uma variável com :.*nº de casas*f. (ARREDONDA O NÚMERO). ex:
linha_1 = f'{nome} tem {altura} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1) 
print(linha_2)
print(linha_3)


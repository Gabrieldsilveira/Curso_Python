# Variáveis são utilizadas para salvar algo na memória do computador
# PEP8: inicie variáveis com letras minúsculas, pode usar números e underline _
# sinal de = é o operador de atribuição, usado para atribuir valor a uma variável
# Uso: nome_variável = expressão
# nome_completo = 'Gabriel Dutra da Silveira'
# idade = 26
# print(nome_completo, idade, sep=('-'))
# # Não queremos ficar repetindo muitos comandos no código, então:
# print(int('1'), type(int('1'))) #podemos atribuir esse valor a uma variável, simplifica o código.

# int_um = int('1') # Daí
# print(int_um, type(int_um))

nome = 'Gabriel Dutra da Silveira'
idade = 26
maior_de_idade = idade >= 18
print('nome:', nome, end= ' - ')
print('idade:', idade)
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')


"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
condicao = 10 == 10
variavel = 'A' if condicao else 'B'
print(variavel)

digito = 9
novo_digito = 0 if digito > 9 else digito
print(novo_digito)
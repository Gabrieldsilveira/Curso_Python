"""
Repetições
while (Enquanto)
Executa uma determinada condição enquanto for verdadeira
Loop infinito -> Quando um código não tem fim
"""

condicao = True

while condicao:
    nome = input('Qual seu nome?: ')
    print(f'Seu nome é {nome}')

    if nome == 'Sair':
        break

print('Acabou')
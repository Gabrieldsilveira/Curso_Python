"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
qnt_linha = 5
qnt_coluna = 5

linha = 1

while linha <= qnt_linha:
    coluna = 1
    while coluna <= qnt_coluna:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1
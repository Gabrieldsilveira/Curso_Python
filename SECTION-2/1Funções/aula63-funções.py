"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parametros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""
# Eu defino as variáveis dentro, a, b, c
def imprimir(a, b, c):
    print(a, b, c)
    

# defino os valores das variáveis criadas la na função
# Cada vez que eu chamar a função, posso ter um valor diferente de acordo com meu algorítimo.
imprimir(1, 2, 3)
imprimir(4, 5, 6)

def saudacao(nome = 'sem nome'):
    print(f'Olá, {nome}')

saudacao('Gabriel')
saudacao('Beatriz')
# funciona exatamente como uma variavel, então se eu nomear la na função
# e nao passar outro valor, ela terá o valor original
saudacao() # Só funciona se eu já tiver nomeado no inicio da função.
"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# Definição da função
def soma(x, y, z):  
    print(f'{x=} y={y} z={z}', '|', 'x + y + z= ', x + y + z)

# NOME DA FUNÇÃO
soma

# EXECUÇÃO DA FUNÇÃO
#    x  y  z
soma(1, 2, 3)
# Posso inverter os valores usando argumentos nomeados
#    y    z    x
soma(y=2, z=3, x=1)
# se eu nomear um argumento do meio(ex), os próximos que vierem precisam ser nomeados
# soma(1, y=2, 3) # Da um erro pois preciso nomear 'z'



# def soma(x, y):
#     # Definição
#     print(x + y)
# print(soma(1, 2)) # retonar 3 e None(por padrão retorna None)

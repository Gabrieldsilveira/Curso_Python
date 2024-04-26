# EXERCÍCIO
# Crie funções que duplicam, triplicam e quiadriplicam
# O número recebido como parâmetro


# n = int(input('Digite o número a ser multiplicado: '))
# m = int(input('Por qual valor multiplicar? [2, 3, 4, 5]: '))
# def Multiplicacao(n):
#     def MultiplicarPorM(m):
#         if m == 2:
#             return n * 2
#         elif m == 3:
#             return n * 3
#         elif m == 4:
#             return n * 4
#         else:
#             return n * 5
#     return MultiplicarPorM
    
# soma = Multiplicacao(n)
# print(f'{n} x {m} = {soma(m)}')

n = int(input('Digite o número a ser multiplicado: '))
m = int(input('Por qual valor multiplicar?: '))
def Multiplicacao(n):
    def MultiplicarPorM(m):
        return n * m
    return MultiplicarPorM
    
soma = Multiplicacao(n)
print(f'{n} x {m} = {soma(m)}')

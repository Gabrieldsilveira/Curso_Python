# Lambda mais complexa

def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_mutiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# essas funções normalmente seriam assim:

print(executa(soma, 2, 3))

print(soma(2, 3))

duplica = cria_mutiplicador(2)
print(duplica(2))

# EM LAMBDA:
# soma
print(executa(lambda x, y: x + y, 2, 2))

# multiplica

duplica = executa(lambda m: lambda n: n * m, 2)
print(duplica(2))

# posso passar *args:

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7, 8, 9
    )
)
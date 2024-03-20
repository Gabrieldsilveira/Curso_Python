# FORMATAÇÃO DE STRINGS USANDO - format(formato)

a = 'A'

b = 'B'

c = 1.1

# Se adicionarmos o . nos mostrará as funções disponíveis

# no format, atribuímos as variáveis que queremos, e na string colocamos {}:
# formato = '{} {} {}'.format(a, b, c,)
# o programa seguirá a ordem, então o primeiro {} será a, o segundo {}, b ...

# Para não depender da ordem, podemos também pegar os valores por índice sempre começando por 0, entao: a= 0; b=1; c=2:
# formato = '{1} {0} {2}'.format(a, b, c,)

# Podemos também nomear as variáveis dentro do format, se nomearmos a primeira, todas as outras deverão ser nomeadas:
# formato = '{nome2} {nome1} {nome3:.2f}'.format(nome1=a, nome2=b, nome3=c,) **OU**

#    string = '{nome2} {nome1} {nome3:.2f}'
#    formato = string.format(nome1=a, nome2=b, nome3=c)

string = '{nome2} {nome3} {nome1}'
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)
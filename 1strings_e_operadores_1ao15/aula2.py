# QUEBRA DE LINHA - nesses casos há a quebra de linha automática, mas os caracteres para quebra de linha são \r e \n -> CRLF
# SEPARAÇÃO DE ARGUMENTOS - São argumentos não nomeados, quando mostrados, há apenas a separação.
print('12', '34') 
# podemos usar o comando sep='' ou sep="", que ira adicionar qualquer coisa no meio para realizar a separação dos itens. EX:
print('56', '78', '2050', sep='-', end='##') # as forquilhas no end, são caracteres que aparecem na leitura, então não há quebra de linha, eles sem juntam.
print('40', '28', '2050', sep='-', end='\n')



"""
split e join com list e str
split - divide uma string (retorna list)
join - une uma string
"""
"""
frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split()
# Se indicarmos um caracter da frase dentro da fnção split, irá quebrar naquele ponto, ou seja
# frase.split(',') --- formariam duas frases. Ex: ['Olha só que', ' coisa interessante']
# O caracter selecionado ',' não foi incluido. PARA TIRAR O ESPAÇO DA LISTA - split(', ') INCLUIR O ESPAÇO NA FUNÇÃO.

print(lista_palavras)
# ['Olha', 'só', 'que,', 'coisa', 'interessante']
"""

"""
MÉTODO strip() -- tira espaços da frase dos dois lados
       ltrip() -- tira espaço do lado esquerdo
       rstrip() - tira espaço do lado direito 
Podemos utilizar esse método para editar uma lista, criando uma nova para preservar os valores da antiga
"""
frase = '     Olha só que  ,      coisa interessante        ' # cheio de espaços
lista_frases_cruas = frase.split(',') # A lista terá muitos espaços. Então criamos uma nova lista para ficar correta

lista_frase = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frase.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas) # ['     Olha só que  ', '      coisa interessante        ']
# print(lista_frase) # ['Olha só que', 'coisa interessante']
frases_unidas = ', '.join(lista_frase)
print(frases_unidas) 
# Olha só que, coisa interessante

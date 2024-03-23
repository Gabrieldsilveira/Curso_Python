"""
Iterável -> str, range, etc (__iter__)
Iterador -> Quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# texto = iter('Gabriel')  #.__iter__()
# print(next(texto)) #.__next__()
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))


#For letra in texto
# texto = 'Gabriel' #iterável
# iteratador = iter(texto) #iterador

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

# O for faz exatamente o que está em cima:
texto = 'Gabriel'  
for letra in texto:
    print(letra)
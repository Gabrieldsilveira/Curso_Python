"""
Introdução ao desempacotamento + tuples (tuplas)
"""
# nomes = ['Beatriz', 'Gabriel', 'Luiz']
# nome1, nome2, nome3 = nomes
# print(nome2)

## OU ##

# nome1, nome2, nome3 = ['Beatriz', 'Gabriel', 'Luiz']
# print(nome2)

# se eu tentar atribuir a variaveis, e tiver mais valores que variáveis, dará erro.
# então eu atribuo o resto a uma variável com (*)antes que vira lista EX:

nome1, *resto = ['Beatriz', 'Gabriel', 'Luiz']
print(nome1, resto)
# o resto vira uma lista com gabriel e luiz

"""
CONVENÇÃO EM PYTHON!!!!
QUANDO EU CRIO UMA VARIÁVEL QUE NAO IREI USAR, USA-SE _ COMO VARIÁVEL PARA DIZER QUE NÃO IRÁ USAR
"""
# _, _, nome3 = ['Beatriz', 'Gabriel', 'Luiz']
# mostro que so irei utilizar "luiz"
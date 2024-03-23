# Operadores in(está entre) e not in(não está entre)
# Strings são iteráveis(pode navegar item por item)

#  0 1 2 3 4 5 6
#  G a b r i e l
# -7-6-5-4-3-2-1
nome = 'Gabriel'
# print(nome[4])
# print(nome[-6])

# print('a' in nome) #Checa se 'a' está entre o nome
# o not in, seria o inverso, ex:

nome = input('Digite um nome: ')
encontrar = input('Digite o que deseja encontrar no nome: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
    

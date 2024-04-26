def MenorArr(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if menor > arr[i]:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def OrdenacaoPorSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = MenorArr(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print(OrdenacaoPorSelecao([3, 5, 1, 2, 6, 7]))

# def pesquisa_binaria(lista, item):
#     baixo = 0
#     alto = len(lista) - 1
#     cont = 0
#     while baixo <= alto:
#         meio = (baixo + alto) // 2
#         chute = lista[meio]
#         if chute == item:
#             return minha_lista[meio]
#         if chute > item:
#             alto = meio - 1
#         else:
#             baixo = meio + 1
#             cont += 1
#     return None

# minha_lista = [1, 2, 3, 5, 7, 9, 11, 12, 16, 21]

# print(pesquisa_binaria(minha_lista, 16))
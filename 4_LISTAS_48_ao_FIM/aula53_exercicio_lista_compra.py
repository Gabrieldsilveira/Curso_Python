"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores de sua lista.
Não permita que o programa quebre com erros
de índices inexistentes na lista.
"""
import os

# Lista principal só é preenchida após apertar 'l', para listar
lista_principal = []
# Looping até apertar l, enquanto isso usuário insere valores à vontade
lista_inserir = []

# tela principal deve estar no looping para usuário utilizar o quanto quiser.

while True:
    # quero imprimir a lista no inicio do programa enumerada apenas se nao estiver vazia.
    if lista_principal:
        for item in enumerate(lista_principal):
            print(item)
    # Entrada para o usuário selecionar uma das opçôes
    print('Selecione uma opção')
    entrada = input('[i]nserir [a]pagar [l]istar: ').lower()
    # se a intrada não for umas das opções oferecidas, informar e voltar ao inicio
    if entrada not in ['i', 'a', 'l']:
        print('Selecione uma das opções')
        continue
    # adicionar item na lista inserir antes de mandar para a principal
    if entrada == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista_inserir.append(valor)
        continue
    # se apertar para apagar, e a lista principal esta vazia, mostra que não há nada para apagar
    # se tiver algo, entra no if e pede um dos numeros dos indices para apagar
    elif entrada == 'a':
        if lista_principal:
            os.system('cls')
            for item in enumerate(lista_principal):
                print(item)
            apagar = input('Selecione um número da lista para apagar: ')
            if apagar.isdigit():
                try:    
                    int_apagar = int(apagar)
                    lista_principal.pop(int_apagar)
                    os.system('cls')
                except IndexError:
                    print('O índice escolhido não existe na lista')
            else:
                print('Digite um dos números da lista.')
                continue
        else:
            print('Não há itens na lista para apagar')
            continue
    # quando selecionar listar, apenas irá listar se tiver itens na lista_inserir, adiciona os itens na principal
    # zera a lista para novos itens
    # se a lista_inserir estiver vazia, informa e volta ao inicio
    elif entrada == 'l' and lista_inserir:
        lista_principal.extend(lista_inserir)
        lista_inserir.clear()
        os.system('cls')
    else:
        print('Não há valor para inserir.')
        continue

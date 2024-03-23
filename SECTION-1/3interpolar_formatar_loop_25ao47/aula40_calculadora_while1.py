while True:
    numero_1 = input('Digite um número: ')
    operador = input('Digite o operador [+ - * /]: ')
    numero_2 = input('Digite o outro número: ')

    if (numero_1.isdigit() and numero_2.isdigit()) and operador == '+':
        int_numero_1 = int(numero_1)
        int_numero_2 = int(numero_2)
        soma = int_numero_1 + int_numero_2
        print(soma)
    elif (numero_1.isdigit() and numero_2.isdigit()) and operador == '-':
        int_numero_1 = int(numero_1)
        int_numero_2 = int(numero_2)
        subtracao = int_numero_1 - int_numero_2
        print(subtracao)
    elif (numero_1.isdigit() and numero_2.isdigit()) and operador == '*':
        int_numero_1 = int(numero_1)
        int_numero_2 = int(numero_2)
        multiplicacao = int_numero_1 * int_numero_2
        print(multiplicacao)
    elif (numero_1.isdigit() and numero_2.isdigit()) and operador == '/':
        int_numero_1 = int(numero_1)
        int_numero_2 = int(numero_2)
        divisao = int_numero_1 / int_numero_2
        print(divisao)
    else:
        print('Você não digitou os números ou os operadores corretamente, tente novamente.')
        continue

    sair = input('Quer sair?: [s]im: ').lower().startswith('s')

    if sair is True:
        break

print('Obrigado por utilizar a minha calculadora!')



   
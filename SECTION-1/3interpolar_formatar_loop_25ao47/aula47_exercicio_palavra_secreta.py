"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os
import random

lista_palavras = ['beatriz', 'honra', 'cerne', 'inato', 'exceto', 'vulgar', 'cetico', 
                  'pressa', 'anexo', 'aniz', 'termo', 'utopia', 'adorno', 'desejo', 
                  'alento', 'indole', 'cortes', 'mazela', 'hostil', 'hetero', 'homem', 'solene',  
                  'fase' ,'ludico', 'difuso', 'zebra', 'alheio', 'torpe', 'perene',
                  'paraquedas', 'ambiçao', 'avestruz', 'veloz', 'jatinho', 'senzala', 'varonil']
palavra_secreta = random.choice(lista_palavras)
letras_acertadas = ''
tentativas = 0
while True:  
    entrada = input('Digite uma letra: ')
    tentativas += 1
    if len(entrada) >= 2:
        print('Digite apenas uma letra.')
        continue
    
    if entrada in palavra_secreta:
        letras_acertadas += entrada

    palavra_formada = ''
    
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    print('Palavra secreta: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era: ', palavra_secreta)
        if tentativas == len(palavra_secreta):
            print('Tentativas: ', tentativas)
            print('parabéns, você ganhou sem erros!')
        else:
            print('Tentativas: ', tentativas)
        break
        
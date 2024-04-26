import os
import time

perguntas = [
    {
        'Pergunta': 'Quanto é 7x6?',
        'Opções': ['36', '48', '44', '42', '38'],
        'Resposta': '42'
    },
    {
        'Pergunta': 'Qual a capital dos Estados Unidos?',
        'Opções': ['Nova Iorque', 'São Francisco', 'Los Angeles', 'Washinton', 'Seattle'],
        'Resposta': 'Washinton'
    },
    {
        'Pergunta': 'Qual a Raiz quadrada de 144?',
        'Opções': ['9', '16', '12', '13', '14'],
        'Resposta': '12'
    },
    {
        'Pergunta': 'Qautos anos tem o Faustão?',
        'Opções': ['65', '73', '59', '79', '77'],
        'Resposta': '73'
    },
    {
        'Pergunta': 'Qual a idade da cidade de Florianópolis?',
        'Opções': ['289', '342', '400', '389', '290'],
        'Resposta': '342'
    }
]

i = 0
cont = 0
pontuacaoFinal = 0
questoes = len(perguntas)
pontuacao = 10 / questoes

while cont < len(perguntas):  
    p = perguntas[i]['Pergunta']
    o = perguntas[i]['Opções']
    r = perguntas[i]['Resposta']

    print(f'Pergunta: {p}')
    print()
    
    print('Opções:')
    for index, valor in enumerate(list(o)):
        print(f'{index}) {valor}')
    
    resp = int(input('Resposta: '))
    resp = o[resp]
    
    if resp == r:
        print('Você acertou!🎉')
        pontuacaoFinal += pontuacao
    else:
        print('Você errou!😓')
    print()
    i += 1
    cont += 1

print('Aguarde enquanto computamos sua nota!')
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
os.system('cls')
print(f'Sua Pontuação foi: {pontuacaoFinal}')
print()
if pontuacaoFinal >= 6:
    print('Parabéns, você passou!!')
else:
    print('Você não passou, tente outra vez.')


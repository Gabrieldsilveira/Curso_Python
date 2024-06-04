import random
import math

def jogo_adivinhacao():
    # Gerar um número aleatório entre 1 e 100
    numero_aleatorio = random.randint(1, 100)
    
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    tentativas_restantes = 5

    while tentativas_restantes > 0:
        # Solicitar a entrada do usuário
        tentativa = int(input("Digite sua tentativa: "))

        # Verificar se a tentativa está correta
        if tentativa == numero_aleatorio:
            print(f"Parabéns! Você acertou o número {numero_aleatorio}!")
            break
        elif tentativa < numero_aleatorio:
            print("Você errou. Tente um número maior.")
        else:
            print("Você errou. Tente um número menor.")

        # Verificar proximidade
        diferenca = abs(numero_aleatorio - tentativa)
        if diferenca <= 10:
            print("Você está muito perto!")

        # Atualizar o número de tentativas restantes
        tentativas_restantes -= 1
        print(f"Tentativas restantes: {tentativas_restantes}")

    if tentativas_restantes == 0:
        print(f"Suas tentativas acabaram. O número correto era {numero_aleatorio}.")

# Chamar a função para iniciar o jogo
jogo_adivinhacao()

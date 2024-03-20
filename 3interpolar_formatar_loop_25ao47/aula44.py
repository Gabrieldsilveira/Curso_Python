"""
For + Range
range -> range(start, stop, step)
start - inicia do numero que determinou
stop - determina onde para
step - de quantos em quantos numero pula
"""

numeros = range(0, 100, 2) #se eu passar apenas um numero ex. (10) eu determino apenas o stop, para no 10, os outros viram 0

for numero in numeros:
    print(numero)
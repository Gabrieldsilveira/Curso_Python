"""
* CONSTANTE (em letras maíusculas)= "Variáveis" que não vão mudar
* Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 60  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega
RANGE_MULTAS = (LOCAL_1 - RADAR_RANGE, LOCAL_1, LOCAL_1 + RADAR_RANGE)

print(f'Velcidade máxima permitida: {RADAR_1}')
if velocidade > RADAR_1 and local_carro in RANGE_MULTAS:
    print(f'O carro passou a: {velocidade}KM/h')
    print('O carro foi multado')
else: 
    print(f'O carro passou a: {velocidade}KM/h')
    print('O carro não foi multado')



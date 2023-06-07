"""
CONSTANTE = "variaveis" que nao vao mudar
usar letra maiuscula para indicar uma constante

Sobre boas maneiras:
muitas condicoes no mesmo if (ruim)
    <- contagem de complexidade (ruim) (quanto mais codigo dentro de codigo, mais complexo fica o codigo e
    complexidade nao eh bom)
"""

velocidade = 61 # velocidade atual do carro
local_carro = 99 # local em que o carro esta na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1= 100 # local onde o radar 1 esta
RADAR_RANGER = 1 # A distancia onde o radar pega

vel_carro_radar = velocidade > RADAR_1
carro_passou_radar = local_carro >= (LOCAL_1 - RADAR_RANGER) and local_carro <= (LOCAL_1 + RADAR_RANGER)
carro_multado_radar = carro_passou_radar and vel_carro_radar

if vel_carro_radar:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar:
    print('Carro passou radar 1')

if  carro_multado_radar:
    print('MULTA!') 
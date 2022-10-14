import math

def valores():
    print("Digite os valores: ")

    valores = []
    while True:
        valor = input()
        if valor == '':
            break
        valores.append(float(valor))

    tamanho = len(valores)

############ MÉDIA ############

soma = 0
for valor in valores:
    soma += valor

print (f'Média = {round(soma, 2)} / {tamanho}')
print (f'Média = {round(soma/tamanho, 2)}')

######### DESVIO MÉDIO ###########

desvio = 0
for valor in valores:
    desvio += abs(valor-media)

print (f'Desvio Médio = {round(desvio, 2)} / {tamanho}')
print (f'Desvio Médio = {round(desvio/tamanho, 2)}')

######### VARIÂNCIA ##############

quadrado_desvio = 0
for valor in valores:
    quadrado_desvios += (valor-media)**2
    
print (f'Variância = {round(quadrado_desvios, 2)} / {len(valores)}')
var = quadrado_desvios/tamanho
print (f'Variância = {round(var, 2)}')

######### DESVIO PADRÃO #########
print(f'Desvio Padrão = {round(math.sqr(var), 2)}')


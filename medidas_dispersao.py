import math

class Medidas_dispersao():
    def __init__(self, valores):
        self.valores = valores
        self.tamanho = len(valores)

############ MÉDIA ############

    def media(self):
        soma = 0
        global media
        soma = sum(self.valores)
        
        print (f'Média = {round(soma, 2)} / {self.tamanho}')
        print (f'Média = {round(soma/self.tamanho, 2)}')
        
        media = soma/self.tamanho
    
######### DESVIO MÉDIO ###########

    def desvio_medio(self):
        desvio = 0
        for valor in self.valores:
            desvio += abs(valor - media)
        
        print (f'Desvio Médio = {round(desvio, 2)} / {self.tamanho}')
        print (f'Desvio Médio = {round(desvio/self.tamanho, 2)}')
    
######### VARIÂNCIA ##############

    def variancia(self):
        quadrado_desvios = 0
        global var
        for valor in self.valores:
            quadrado_desvios += (valor - media)**2
    
        print (f'Variância = {round(quadrado_desvios, 2)} / {self.tamanho}')
        var = quadrado_desvios/self.tamanho
        print (f'Variância = {round(var, 2)}')
        
######### DESVIO PADRÃO #########

    def desvio_padrao(self):
        print(f'Desvio Padrão = {round(math.sqrt(var), 2)}')

if __name__ == '__main__':
    a = Medidas_dispersao([1,3,4])
    a.media()
    a.desvio_medio()
    a.variancia()
    a.desvio_padrao()

from . import Medidas_dispersao

print(
'1 - Medidas de dispersão' /n
)
opcao = input("Digite a opção")

if opcao == '1':
    print("Medidas de dispersão /n",
    "Digite os valores: ")
    valores = []
    while True:
        valor = input()
        if not valor.isdigit():
            break
        valores.append(float(valor))
    a = Medidas_dispersao()
    a.media()
    a.desvio_medio()
    a.variancia()
    a.desvio_padrao()

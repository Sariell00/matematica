import medidas_dispersao as md

print(
'1 - Medidas de dispersão\n'
)
opcao = input("Digite a opção: ")

if opcao == '1':
    print("Digite os valores: ")
    valores = []
    while True:
        valor = input()
        if not valor.isdigit():
            break
        valores.append(float(valor))
    a = md.Medidas_dispersao(valores)
    a.media()
    a.desvio_medio()
    a.variancia()
    a.desvio_padrao()

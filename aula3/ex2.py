numero = int(input('Quantas linhas você quer? '))

linha = 1
contador = 1

for i in range(numero):
    coluna = 1
    while coluna <= linha:
        print(contador, end=' ')
        contador += 1
        coluna += 1
    print()
    linha += 1

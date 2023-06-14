from mercado import *

while True:
    print("Bem vindo ao mercado, que precinho")
    print("1 - Para comprar")
    print("2 - Para sacar dindin")
    print("3 - Para sair do mercado")

    op = int(input("O que você deseja fazer? "))
    
    # Verifica a opção escolhida pelo usuário
    match op:
        case 1:
            dinheiro = float(input("Quanto de dinheiro você tem? "))  # Solicita o valor do dinheiro disponível
            produto = input("Qual produto você quer comprar? ")  # Solicita o nome do produto a ser comprado
            quantidade = int(input("Qual a quantidade que você quer comprar? "))  # Solicita a quantidade do produto a ser comprado
            resultado = comprar(dinheiro=dinheiro, produto=produto, quantidade=quantidade)  # Chama a função comprar() para realizar a compra
            print(resultado)  # Exibe o resultado da compra
        case 2:
            valor = float(input("Quanto você quer sacar? "))  # Solicita o valor a ser sacado
            sacar_dinheiro(valor)  # Chama a função sacar_dinheiro() para exibir as notas necessárias
        case 3:
            resultado = sair()  # Chama a função sair() para encerrar o programa
            print(resultado)  # Exibe a mensagem de saída do mercado
    break 
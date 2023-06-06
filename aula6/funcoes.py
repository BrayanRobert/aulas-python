# Funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas permitem que você divida seu código em partes menores e mais gerenciáveis, tornando-o mais organizado e fácil de entender.
from sistema import *
while True:
    print("BEM VINDO AO MERCADO DO GIRINO, ONDE A INFLAÇÃO NÃO EXISTE")
    print("1- Para comprar")
    print("2- Para sacar dinheiro")
    print("3- Para sair do mercado")

    op = int(input("O que você deseja fazer? "))

    match op:
        case 1:
            dinheiro = float(input("Quanto de dinheiro você tem? "))
            produto = input("Qual produto você quer comprar? ")
            quantidade = int(input("Qual a quantidade que você quer comprar? "))
            cancelamento = cancelar(produto=produto, quantidade=quantidade)
            print(f"O troco que você recebeu foi {troco(dinheiro=dinheiro, produto=produto, quantidade=quantidade)}")
            resultado = comprar(dinheiro=dinheiro, produto=produto, quantidade=quantidade)
            print(resultado)
        case 2:
           dinheiro = float(input("Quanto de dinheiro você tem? "))

           resultado = sacar(dinheiro=dinheiro)
           print(resultado)
        case 3:
            resultado = sair()
            print(resultado)
            break 
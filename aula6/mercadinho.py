from funcoes import *

while True:
    print("BIENVENIDO A LO MERCADITO HERMANO!")
    print("1 - Comprar")
    print("2 - Sacar dinheiro")
    print("3 - Sair")

    op = int(input("Qual a boa?:"))

    match op:
        case 1:
            dinheiro = float(input("Tu tem quanto ai?"))
            mercadoria = input("O que voce quer comprar?")
            quantidade = int(input("Quantos produtos voce quer?"))
            resultado = comprar(dinheiro = dinheiro, mercadoria = mercadoria, quantidade = quantidade)
            print(resultado)
        case 2:
            dinheiro = float(input("Tu tem quanto de grana ai?"))
            resultado = sacar(dinheiro = dinheiro)
            print(resultado)
        case 3:
            resultado = sair()
            print(resultado)
            break
        
# Fazendo uma calculadora
valor1 = int(input("Qual o primeiro valor? "))
valor2 = int(input("Qual o segundo valor? "))
operacoes = {"+" : f"{valor1+valor2}", "-" : f"{valor1-valor2}", "*" : f"{valor1*valor2}", "/" : f"{valor1/valor2}", "" : "ERRO! ISSO TA VAZIO"}
op = input("Digite a operação que vc deseja: ")
print(operacoes[op])


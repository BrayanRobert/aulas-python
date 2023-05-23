valor1 = int(input("Digite o primeiro valor:"))
valor2 = int(input("Digite o segundo valor:"))
op = input("digite a operação que voce deseja: ")
operacoes = {
    "+" :f"{valor1 + valor2}",
    "-" :f"{valor1 - valor2}",

}
print(operacoes[op])
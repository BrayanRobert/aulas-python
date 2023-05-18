# Faça um programa que simule uma calculadora polonesa.
# 2 + 3 = 2 3 +
# 10 / 5 = 10 5 /
# 3 * 3 = 3 3 *
# 100 - 50 = 100 50 -

# numero1 = float(input("Digite o primeiro numero: "))
# numero2 = float(input("Digite o segundo numero: "))

# op = input("Digite a operação matematica que você deseja realizar: ")

numero1,numero2,op = input("Digite os numeros e a operação separadas por um espaço: ").split(" ")

numero1 = float(numero1)
numero2 = float(numero2)

if op == '+':
    soma = numero1 + numero2
    print(f"A soma é: {soma}")
elif op == '-':
    sub = numero1 - numero2
    print(f"A subtração é: {sub}")
elif op == '*':
    mult = numero1 * numero2
    print(f"A multiplicação é: {mult}")
elif op == '/':
    div = numero1 / numero2
    print(f"A divisão é: {div}")
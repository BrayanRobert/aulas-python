#escreva um programa que leia uma lista e imprima na tela a média aritimética dessa lista

numeros =[ 999, 666, 333, 777]

for i in range(len(numeros)):
    numero = numeros[i]

    if numero%2 == 0:
        print(f"{numero} esse número é par")
    else:
        print(f"{numero} esse número é impar")
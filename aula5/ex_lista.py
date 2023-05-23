# Escreva um programa que leia uma lista e imprima na tela a média aritmética dessa lista

lista = [10, 20, 30, 40, 75, 67]
soma = 0

for i in range(len(lista)):
    valor = lista[i]
    soma += valor

print(f"A média é {soma/len(lista)}")

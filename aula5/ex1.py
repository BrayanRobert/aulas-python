# Escreva um programa que leia uma lista e imprima na tela a média aritmética dessa lista

media = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 81, 19, 20]
soma = 0

for i in range(len(media)):
    soma = soma + media[i]

print(f"A media é: {soma/len(media)}")

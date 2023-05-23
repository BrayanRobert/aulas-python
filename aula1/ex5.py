# Escreva um programa que leia uma lista e imprima na tela a média aritmética dessa lista

lista = []
num_notas = int(input("Digite quantas notas você tem: "))

for _ in range(num_notas):
    nota = float(input("Digite uma nota: "))
    lista.append(nota)

soma = sum(lista)
media = soma / len(lista)
print("A média aritmética da lista é: {:.2f}".format(media))
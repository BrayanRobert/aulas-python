# Faça um programa que pegue o nome do aluno, receba duas notas que ele teve em uma prova, e faça a média dessas notas, se a média for
# maior ou igual a 7, mostre que ele foi aprovado, se a média, ficou maior ou igual a 3, porém menor que 7, mostre que ele foi pra rec
# se a nota for maior que 7, mostre que ele foi aprovado, se a média, ficou maior.
nome = input("Digite seu nome")
nota1 = float(input("Digite sua nota 1"))
nota2 = float(input("Digite sua nota 2"))

media = (nota1 + nota2)/2

if media >=7:
    print(f'Voce foi aprovado {nome}')
elif media >=3 and media <7:
    print(f'Voce está de recuperação {nome}')
else:
    print(f'Voce foi reprovado {nome}')




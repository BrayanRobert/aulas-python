# Faça um programa que pegue o nome do aluno, receba duas notas que ele teve em uma prova, e faça a média dessas notas, se a média for
# maior ou igual a 7, mostre que ele foi aprovado, se a média, ficou maior ou igual a 3, porém menor que 7, mostre que ele foi pra rec
# se a nota for maior que 7, mostre que ele foi aprovado, se a média, ficou maior.
nome = input("Qual é seu nome ?")

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
  
media = (nota1 + nota2) / 2

    
if media < 7.0:
        print(f'{nome},sua media é {media} e está Reprovado')
elif media < 10:
        print(f'{nome},sua media é {media} está Aprovado')
else:
        print(f'{nome},sua media é {media} está Aprovado acima da media!')
# Faça um programa que pegue o nome do aluno, receba duas notas que ele teve em uma prova, e faça a média dessas notas, se a média for
# maior ou igual a 7, mostre que ele foi aprovado, se a média, ficou maior ou igual a 3, porém menor que 7, mostre que ele foi pra rec
# se a nota for maior que 7, mostre que ele foi aprovado, se a média, ficou maior
nome= input('Olá, qual é o seu nome ? ')
nota1= float(input(f'{nome}, me informe a nota da primeira prova do trimestre: '))
nota2= float(input('Agora a nota da segunda prova: '))
media= float((nota1+nota2)/2)

if media >=7:
       print(f'{nome}, sua média é {media} . Parabéns, você foi aprovado!!!! ')
elif media >= 3:
       print(f'{nome}, sua média é {media} . Você está de recuperação.')
elif media <3:
       print(f'{nome}, sua média é {media} . Sinto muito, mas você está reprovado. ')       
  




# Faça um programa que pegue o nome do aluno, receba duas notas que ele teve em uma prova, e faça a média dessas notas, se a média for
# maior ou igual a 7, mostre que ele foi aprovado, se a média, ficou maior ou igual a 3, porém menor que 7, mostre que ele foi pra rec
# se a nota for maior que 7, mostre que ele foi aprovado, se a média, ficou maior

Name = input('Who are you?')

firstresult = float(input('First Result ='))

secondresult = float(input('Second Result ='))

average = (firstresult+secondresult)/2

if average >= 7:
    print("aprroveeed vagabundo")

else:
    print("not aprovveeedd")

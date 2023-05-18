# Faça um programa que pegue o nome do aluno, receba duas notas que ele teve em uma prova, e faça a média dessas notas, se a média for
# maior ou igual a 7, mostre que ele foi aprovado, se a média, ficou maior ou igual a 3, porém menor que 7, mostre que ele foi pra rec
# se a nota for maior que 7, mostre que ele foi aprovado, se a média, ficou maior

# Notas : Variação de zero até dez! podendo conter números quebrados, 6.8, 9.7...

nome = input('Diga seu nome: ')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1+nota2)/2

if (nota1 or nota2) < 0 or (nota1 or nota2) > 10:
    print('erro! nenhuma de suas notas podem ser maior que dez, ou menor que zero')
    print('Por favor, digite suas notas certas, no intervalo de zero a dez')
    nota1 = float(input('Digite sua primeira nota: '))
    nota2 = float(input('Digite sua segunda nota: '))
    media = (nota1+nota2)/2
    if media >= 7:
        print(' ,você foi aprovado!')
    elif media >= 3 and media < 7:
        print(' ,você foi para a recuperação')
    else:
        print(' ,você foi expulso pelo marlon')
else:
    if media >= 7:
        print('Você foi aprovado, ' +nome)
    elif media >= 3 and media < 7:
        print('Você foi para a recuperação, '+nome)
    else:
        print('Você foi expulso pelo marlon, ' +nome)
#programa para calcular média e dizer se o aluno fou aprovado ou não

nome = input('Digite o nome do aluno:')
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1+nota2)/2
if media >= 7.0:
    print(f'Parabéns {nome}, voce foi aprovado com média igual a: {media}')
elif media >= 3 and media < 7:
    print(f'{nome}, voce esta de exame final com média: {media}')
else:
    print(f'{nome}, voce esta reprovado com média: {media}')
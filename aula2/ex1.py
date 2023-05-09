# Faça um programa que pegue o nome do aluno, receba duas notas que ele teve em uma prova, e faça a média dessas notas, se a média for
# maior ou igual a 7, mostre que ele foi aprovado, se a média, ficou maior ou igual a 3, porém menor que 7, mostre que ele foi pra rec
# se a nota for maior que 7, mostre que ele foi aprovado, se a média, ficou maior

#================== CENÁRIO 1 ==================#

aluno = "Brayan Robert"
nota1 = 0
nota2 = 0
media = (nota1+nota2)/2

if(media>=7):
  print(f"O aluno {aluno} está Aprovado!")
elif(media>=3 and media<7):
  print(f"O aluno {aluno} está de Recuperação!")
else:
  print(f"O aluno {aluno} está fora das médias, deverá ser expulso da instituição!")

#===============================================#

#Vai fazer um programa que vai pegar o nome do aluno e pegar duas notas.
#Vai fazer a média das notas.
#Se for maior que 7, aprovado.
#Se estiver entre 3 e 7, recuperação.
#Se estiver menos de 3, reprovado.
# Notas : Variação de zero até dez! podendo conter números quebrados, 6.8, 9.7...
nota1 = float(input("Resultado do Teste"))
nota2 = float(input("Resultado da Prova"))
nota3 = nota1 + nota2
média = nota3/2
print("Sua média é", média)
if média >=7: 
    print("Você está aprovado")
elif média >=3:
    print("Você está em recuperação")
else:
    print("Você está reprovado")
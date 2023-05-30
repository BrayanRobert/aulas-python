# Pergunte ao usuário qual o nome dele e imprima uma mensagem de boas vindas
nota1 = float(input("Resultado do Teste"))
nota2 = float(input("Resultado da Prova"))
nota3 = nota1 + nota2
média = nota3/2
print("Sua média é", média)
if média >=7: 
    print("Aprovado")
elif média >=3:
    print("Recuperação")
else:
    print("Reprovado")
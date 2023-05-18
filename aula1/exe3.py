# Peça para o usuário inserir a base e altura de um retângulo e imprima sua área
base = int(input("Digite a base do retângulo "))

altura = int(input("Digite a altura do retângulo "))

multiplicacao = int(base * altura)

String1 = ("A base do retângulo é ")
String2 = base
String3 = String1 + str(String2)
print(String3)
String4 = ("A altura do retângulo é ")
String5 = altura
String6 = String4 + str(String5)
print(String6)
String7 = ("Agora se multiplicarmos os dois valores obteremos a área que é ")
String8 =  String7 + str(multiplicacao)
print(String8)
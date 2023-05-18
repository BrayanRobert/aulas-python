# Faça um programa que simule uma calculadora polonesa.
# 2 + 3 = 2 3 +
# 10 / 5 = 10 5 /
# 3 * 3 = 3 3 *
# 100 - 50 = 100 50 -

Nome = input('Olá, qual o seu nome?: ')
print(f'É um prazer lhe conhecer, {Nome} !!!')
print(f'{Nome}, hoje você irá testar nossa calculadora polonesa.')

resposta = input("Você sabe como ela funciona? (sim/não): ")

if resposta == "sim":
    print("Então vamos lá!!!")
elif resposta == "não":
    print("Ah, tudo bem. De uma olhada no site https://definirtec.com/notacao-polonesa-reversa-rpn/, e depois volte para o exercicio !.")
else:
    print("Desculpe, não entendi sua resposta.")

while True:
    cancelar = input(' Caso não queira mais usar a calculadora digite cancelar.')  
    if cancelar == "cancelar":
        break
    n1 = int(input(' Digite o número de um operador: '))
    n2 = int(input('Digite o segundo número: '))
    operação = (input('Digite o operador aritimético desejado: ')) 
    if operação == '+':
        print(f"{n1} {n2} + = {n1+n2}") 
    elif operação == '-':
        print(f"{n1} {n2} - = {n1-n2}")
    elif operação == '/':
        print(f"{n1} {n2} / = {n1/n2}")
    elif operação == '*':
        print(f"{n1} {n2} * = {n1*n2}")
    
    else: 
        print("Digite somente esses operadores: /, *, -, +")






 
    
    



    



   


    





    

    


        



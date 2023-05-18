# Faça um programa que simule uma calculadora polonesa.
# 2 + 3 = 2 3 +
# 10 / 5 = 10 5 /
# 3 * 3 = 3 3 *
# 100 - 50 = 100 50 -
import time
Nome = input('Olá, qual o seu nome?: ')
time.sleep(1.5)
print(f'É um prazer lhe conhecer, {Nome} !!!')
time.sleep(2.5)
print(f'{Nome}, hoje você irá testar nossa calculadora polonesa.')
time.sleep(2.5)
resposta = input("Você sabe como ela funciona? (sim/não): ")

if resposta == "sim":
    time.sleep(1.5)
    print("Então vamos lá!!!")
    time.sleep(1.5)
elif resposta == "não":
    time.sleep(1.5)
    print("Ah, tudo bem. De uma olhada no site https://definirtec.com/notacao-polonesa-reversa-rpn/, e depois volte para o exercicio !.")
else:
    time.sleep(1.5)
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






 
    
    



    



   


    





    

    


        



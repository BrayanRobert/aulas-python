# Faça um programa que dê ao usuário 4 opções:
# 1 - Somar 2 + 2. 2 - Multiplicar 3 vezes 5, 3 - Mostra que é rio de janeiro, 4 - Sair do programa
print('1- corresponde a soma de 2+2')
print('2- corresponde a multiplicação de 3x5')
print('3- corresponde a sua localização')
print('4- fecha o programa.')
while True:
   
    op = int(input('Digite uma opção de 1 a 4 onde: '))
    
    if op == 1:
        print(f'{2+2}')
    elif op == 2:
        print (f'{3*5}') 
    elif op== 3:
        print('Aqui é Rio de Janeiro') 
    elif op== 4:
        break    
    
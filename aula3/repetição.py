while True:
    print('Escolha uma opção:')
    print(' 1 - somar 2+2')
    print('2 - multiplicar 3 x 5')
    print('3 - mostrar Rio de janeiro')
    print('4 - Sair do programa')

    op =  int(input('Digite a opção desejada'))
    if op ==1:
        print("2+2", 2+2)
    elif op == 2:
        print ("3 x 5 =", 3*5)
    elif op == 3:
        print("Rio de janeiro")
    elif op ==4:
        print("Saindo do programa")
    break

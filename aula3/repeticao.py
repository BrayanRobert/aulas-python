# Aula 3 - Laços de repetição

nome = 'marlon' # string do tamanho 6

for i in range(len(nome)): # len(nome) = 6
    print(nome[i])


contador = 0
ola = 0
while True:
    ola += 2
    contador += ola*ola*ola*ola*ola*ola*ola*30002392039*ola
    print(contador)


for x in range(5000):
    numero = (x*x) + x*5 + 700

    if numero >= 1000000:
        print(f'O x mínimo para satisfazer essa condição é {x}, e o valor que ele retorna na função é {numero}')
        break
    else:
        continue

while True:
    op = int(input('Digite uma opção: '))

    if op == 1:
        print('Ola, mundo!')
    elif op == 2:
        print('Vai tomar no cu mundo')
    elif op == 3:
        break

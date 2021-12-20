# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for i in range(1, 10):
        print(f'{n} x {i} = {n * i}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
print('THE END.')
    
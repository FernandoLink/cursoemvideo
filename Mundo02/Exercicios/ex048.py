# Faça um programa que calcule a soma entre os números ímpares que são múltimplos de três e que se encontram no intervalo de 1 até 500.
cont = 0
soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont += 1
        soma += i
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))
        
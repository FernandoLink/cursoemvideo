# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digital foi {} e a sua porção inteira é {}.'.format(num, trunc(num)))
print('O valor digital foi {} e a sua porção inteira é {}.'.format(num, int(num)))

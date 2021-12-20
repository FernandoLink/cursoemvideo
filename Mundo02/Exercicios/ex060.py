# Faça um programa que leia um número qualquer e mostre seu fatorial.
from math import factorial
n = int(input('Digite um número para descobrir o seu fatorial: '))
print('O fatorial de {} é {}.'.format(n, factorial(n)))

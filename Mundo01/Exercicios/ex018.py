# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, cos, sin, tan
ang = float(input('Digite o ângulo que você deseja: '))
print('COSSENO: {:.2f}'.format(cos(radians(ang))))
print('SENO: {:.2f}'.format(sin(radians(ang))))
print('TANGENTE: {:.2f}'.format(tan(radians(ang))))

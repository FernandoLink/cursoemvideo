# Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print('A hiponetusa vai medir {:.2f}.'.format(hypot(co, ca)))

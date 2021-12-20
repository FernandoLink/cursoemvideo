# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < c and b < c: menor = b
if c < a and c < b: menor = c
maior = a
if b > c and b > c: maior = b
if c > a and c > b: maior = c
print('Menor: {}'.format(menor))
print('Maior: {}'.format(maior))

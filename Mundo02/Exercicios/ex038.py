# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
if primeiro > segundo:
    print('Primeiro valor é maior.')
elif segundo > primeiro:
    print('Segundo valor é maior.')
else: 
    print('Valores iguais')
  
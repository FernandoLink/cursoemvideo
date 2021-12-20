# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep

cont = 0
lista = list()

print('-' * 30)
print(f'{"JOGOS DA LOTOFÁCIL":^30}')
print('-' * 30)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, qtd):
    while True:
        num = randint(1, 25)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont > 14:
            break
    lista.sort()
    print(f'Jogo {c+1}: {lista}')     
    lista.clear()   
    cont = 0
    sleep(2)

print(f'{" THE END ":-^40}')

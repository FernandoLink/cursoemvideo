# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def theEnd():
    print(f'{" THE END ":-^40}')
    
    
def maior(* números):
    print('-=' * 30)
    print('Analisando os valores passado...')
    maior = 0
    for k, v in enumerate(números):
        if k == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        print(f'{v} ', end='', flush=True)
        sleep(0.3)
    print(f'Foram informados {len(números)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    
    
maior(2, 9, 4, 5, 7, 1)    
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
theEnd()    

# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo desconsiderando os espaços.
# apos a sopa
# a sacada da casa
# a torre da derrota
# o lobo ama o bolo
# anotaram a data da maratona
frase = str(input('Digite uma frase: ')).strip().upper()
junto = ''.join(frase.split())

# outra forma mais simples sem utilizar o for
inverso = junto[::-1]

'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
    
print('O inverso de {} é {}'.format(junto, inverso))    
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

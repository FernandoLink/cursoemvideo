# Faça um programa que tenha uma função área, que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def theEnd():
    print(f'{" THE END ":-^40}')


def área(l, c):    
    a = l * c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {a:.1f}m²')
    
print(' Controle de Terrenos')    
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
área(largura, comprimento)

theEnd()  

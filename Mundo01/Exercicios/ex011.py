# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada livro de tinta, pinta uma área de 2m²
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
área = largura * altura
tinta = área / 2
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m²'.format(largura, altura, área))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(tinta))

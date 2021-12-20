# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
celsius = float(input('Informe a temperatura em °C: '))
fahrenheit = 9 * celsius / 5 + 32
print('A temperatura de {:.2f}°C corresponde a {:.2f}°F'.format(celsius, fahrenheit))

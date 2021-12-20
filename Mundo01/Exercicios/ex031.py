# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$ 0.50 por km para viagens de até 200km e R$0.45 para viagens mais longas.
distancia = float(input('Qual a distância da sua viagem? '))
print('R$ {}'.format(distancia * 0.50 if distancia <= 200 else distancia * 0.45))

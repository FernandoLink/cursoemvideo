# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = float(input('Quantos anos de financiamento? '))

prestacao = casa / (anos * 12)
minimo = salario * 30 /100

if prestacao <= minimo:
    print('Empréstimo CONCEDIDO')
else:
    print('Empréstimo NEGADO')
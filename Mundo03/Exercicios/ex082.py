# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

valores = list()
pares = list()
impares = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    if valores[-1] % 2 == 0:
        pares.append(valores[-1])
    else:
        impares.append(valores[-1])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Lista = {valores}')
print(f'Pares = {pares}')
print(f'Impares = {impares}')
print(f'{" THE END ":-^40}')

# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input('Digite o {c}o. um valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)

núm[0].sort()
núm[1].sort()

print('-=' * 30)
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')
print(f'{" THE END ":-^40}')

# Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = terceira = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2:
            terceira += matriz[l][c]
        if l == 1 and c == 0:
            maior = matriz[l][c]
        else:
            if l == 1 and matriz[l][c] > maior:
                maior = matriz[l][c]
    print()
print('-=' * 30)        
print(f'A soma de todos os valores digitados é {soma}')
print(f'A soma dos valores da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha é {maior}')

print(f'{" THE END ":-^40}')

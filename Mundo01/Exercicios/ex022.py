# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maísculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.
nome = str(input('Nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(' '))
print(nome.find(' '))

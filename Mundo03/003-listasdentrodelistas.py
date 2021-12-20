pessoas=[['Pedro', 25], ['Maria', 19],['João', 32]]
print(pessoas)
print(pessoas[0])
print(pessoas[0][1])
print(pessoas[2][0])

pessoas.append(['Fernando', 51])
print(pessoas)

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos.')

print(f'{" THE END ":-^40}')
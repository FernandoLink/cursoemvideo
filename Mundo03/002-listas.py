# As listas são mutáveis
# Muito importante a = b ela cria uma ligação, se alterar b altera também no a
# b = a[:] cria uma cópia da a na b, se alterar a b não altera a a
lanche = ['hamburguer', 'suco', 'pizza', 'pudim','batata frita']
print(lanche)
lanche.append('sorvete')
print(lanche)
lanche.insert(0, 'chocolate')
print(lanche)
del lanche[3]
print(lanche)
lanche.pop(3)
print(lanche)
lanche.remove('batata frita')
print(lanche)
lanche.sort()
print(lanche)
lanche.sort(reverse=True)
print(lanche)

for c, v in enumerate(lanche):
    print(f'Na posição {c} encontrei o valor {v}.')

print(f'\n{" THE END ":-^40}')

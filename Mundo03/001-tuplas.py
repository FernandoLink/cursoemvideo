# As tuplas () são IMUTÁVEIS
# lista []
# dicionário {}

lanche = ('hamburguer', 'suco', 'pizza', 'pudim','batata frita')

print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[0:2])
print(lanche[:2])
print(lanche[2:])

for comida in lanche:
    print(f'Eu vou comer {comida}')
    
for pos, comida in enumerate(lanche) :
    print(f'Eu vou comer {comida} na {pos}')
    
# Pode ordenar mas não modifica a tupla, tuplas são imutáveis  
print(sorted(lanche))  
print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5))
print(c.index(8))

# Tuplas são imutáveis mas podemos apagar da memória
pessoa = ('Fernando', 51, 'M')
print(pessoa)
del(pessoa) 
    
print('{:-^30}'.format(' THE END '))

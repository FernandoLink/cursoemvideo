# Primeiro exemplo de if
tempo = int(input("quantos anos tem o seu carro? "))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')

# Segundo exemplo de if
print('carro novo' if tempo <= 3 else 'carro velho')    

# Terceiro exemplo de if
nome = str(input('Qual é seu nome? '))
if nome == 'Fernando':
    print('Que nome lindo você tem')
else:
    print('Seu nome é tão normal')
print('Bom dia, {}'.format(nome))

# Quarto exemplo de if
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('sua média foi boa! PARABÉNS!')
else:
    print('Sua média foir ruim! ESTUDE MAIS!') 

print('--FIM--')


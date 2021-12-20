def mostraLinha():
    print('-' * 40)


def mensagem(msg):
    print('-' * 40)
    print(f'{msg:^40}')
    print('-' * 40)
 
    
def theEnd():
    print(f'{" THE END ":-^40}')
 
 
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
    
    
def contador(* num):
    print(num) # cria uma tupla
    

def dobra(valores):
    pos = 0
    while pos < len(valores):
        valores[pos] *= 2
        pos += 1
    
mostraLinha()
mensagem('FERNANDO LINK')
mostraLinha()
soma(7, 3)
soma(b=7, a=3)
mostraLinha()
contador(2, 1, 7)
contador(4, 4, 7, 6, 2)
mostraLinha()
valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)
mostraLinha()

theEnd()

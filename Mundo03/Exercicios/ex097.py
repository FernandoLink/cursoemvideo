# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.   
def theEnd():
    print(f'{" THE END ":-^40}')
   

def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


escreva('Fernando Link')    
escreva('No Pain No Gain So Shut Up and Train')
theEnd()    

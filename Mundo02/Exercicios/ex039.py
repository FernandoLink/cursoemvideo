# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou o tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

nasc = int(input('Ano de nascimento: '))

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, date.today().year - nasc, date.today().year))
if date.today().year - nasc == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif date.today().year - nasc < 18:
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(18 - date.today().year - nasc))
    print('Seu alistamento será em {}.'.format(date.today().year + (18 - date.today().year - nasc)))
else:
    print('Você já deveria ter se alistado há {} anos.'.format(date.today().year - nasc - 18))
    print('Seu alistamento será em {}.'.format(date.today().year - (date.today().year - nasc - 18)))

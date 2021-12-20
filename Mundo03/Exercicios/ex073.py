# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time Chapecoense.
times = ('Atlético Paranaense', 'São Caetano', 'São Paulo', 'Palmeiras', 'Flamengo', 'Internacional', 'Coritiba', 'Fluminense','Chapecoense','Corinthians'
          'Santos', 'Botafogo', 'Avaí', 'Atlético Mineiro', 'Vasco', 'Grêmio', 'Bahia', 'Fortaleza', 'Ponte Preta', 'Sport')
print('-=' * 30)
print(f'Lista de times: {times}')
print('-=' * 30)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 30)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 30)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição.')
print('-=' * 30)
print('{:-^30}'.format(' THE END '))

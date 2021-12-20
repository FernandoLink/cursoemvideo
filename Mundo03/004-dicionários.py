pessoas ={'nome': 'Fernando', 'sexo': 'M', 'idade': 51}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas)
print(pessoas['nome'])
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())  

for k in pessoas.keys():
    print(k)   
for v in pessoas.values():
    print(v)      
for k,v in pessoas.items():
    print(k,v)    
    
brasil = []    
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}      
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}      
print(estado1,estado2)
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])

print(f'{" THE END ":-^40}')

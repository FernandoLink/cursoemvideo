frase = '   Fernando Link Valeria souza link henrique souza link'

print(frase)
print(frase[9])
print(frase[9:12])
print(frase[0:21:2])
print(frase[:5])
print(frase[9:])
print(frase[1::3])

print(len(frase))
print(frase.count('n'))
print(frase.count('n',0,4))
print(frase.find('Link'))
print(frase.find('Android'))
print('Link' in frase)
print(frase.upper().count('I'))

print(frase.replace('Link','Python'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.lstrip())

dividido = frase.split()
print(dividido)
print(dividido[3][3])


print('-'.join(frase))

print("""asdfaf asçldfkj asçdlfkjasdf çlkajsdf çlaskdf çalskfjd asçldfjk asçdlfkjaçsd klfjçlasdkjf asdf
      çalskfjdçalskdfj açsdlfjk açsdlfj adfçjk asdfçlaskj fdçaslfjd açlsdkfj afd""")

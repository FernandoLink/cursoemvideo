# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('{}km\n{}hm\n{}dam\n{}m\n{}dm\n{}cm\n{}mm\n'.format(km, hm, dam, m, dm, cm, mm))

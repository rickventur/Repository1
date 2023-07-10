# Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo

n = int(input('Digite o valor a ser verificado: '))

if n >= 0:
    print('O numero {} é positivo!'.format(n))
else:
    print('O numero {} é negativo!'.format(n))
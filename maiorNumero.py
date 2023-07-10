# Faça um programa e peça dois números e imprima o maior deles

n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))

if n1 > n2:
    print('O maior número entre {} e {} é {}'.format(n1, n2, n1))
else:
    print('O maior número entre {} e {} é {}'.format(n1, n2, n2))
dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
s = (dias * 60) + (km * 0.15)
print('O total a se pagar é de R${}'.format(s))
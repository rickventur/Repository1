salario = float(input('Qual o salário do funcionário? R$'))
s = salario + salario * 15 / 100
print('O salario do funcionário com 15% de aumento ficara R${:.7}0'.format(s))
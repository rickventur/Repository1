from datetime import date

ano = int(input('Qual ano você quer analisar? (Coloque 0 para analisar o ano atual) '))

if 0 == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: 
    print('O ano {} BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
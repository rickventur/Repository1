nome = str(input('Qual o nome do produto? '))
categoria = str(input('Qual a categoria do produto? '))
quantidade = int(input('Quala a quantidade do produto? '))

if nome and categoria and quantidade:
    if 'Alimento' in categoria:
        if quantidade < 50: 
            print('Solicitar {} a equipe de compras temos apenas {} unidades!'.format(nome, quantidade))
    elif 'Bebida' in categoria:
        if quantidade < 75: 
            print('Solicitar {} a equipe de compras temos apenas {} unidades!'.format(nome, quantidade))
    elif 'Limpeza' in categoria:
        if quantidade < 30: 
            print('Solicitar {} a equipe de compras temos apenas {} unidades!'.format(nome, quantidade))
else:
    print('Preencha os espaços corretamente!')
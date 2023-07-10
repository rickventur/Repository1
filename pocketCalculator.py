print(' '*15)
print('Cálculadora Automatica.')
print('_'*15)

res = str(input('Calcular: '))

def __calcular__():
    if '+' in res:
        calculo = res.split('+')
        a = int(calculo[0])
        b = int(calculo[1])
        resultado = a + b
        print(f'A soma entre {a} e {b} é {resultado}')
    elif '-' in res:
        calculo = res.split('-')
        a = int(calculo[0])
        b = int(calculo[1])
        resultado = a - b
        print(f'A subtração entre {a} e {b} é {resultado}')
    elif '*' in res:
        calculo = res.split('*')
        a = int(calculo[0])
        b = int(calculo[1])
        resultado = a * b
        print(f'A multiplicação entre {a} e {b} é {resultado}')
    elif '/' in res:
        calculo = res.split('/')
        a = int(calculo[0])
        b = int(calculo[1])
        resultado = a / b
        print(f'A divisão entre {a} e {b} é {resultado}')
    elif '%' in res:
        calculo = res.split('%')
        a = int(calculo[0])
        resultado = a % 2
        print(f'O módulo de {a} tem {resultado} como resultado.')

__calcular__()


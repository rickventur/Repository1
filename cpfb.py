cpf = str(input('Insira seu CPF: '))

if cpf.strip(' ', '.', ',', '-', '_'):
    print(cpf)
if len(cpf) == 11:
    if cpf.isnumeric() == True:
        print('Verificar')
else:
    print('Digite seu CPF corretamente e digite apenas números')
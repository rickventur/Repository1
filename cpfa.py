cpf = str(input('Insira seu CPF (digite apenas números): '))

if len(cpf) == 11 and cpf.isnumeric():
        print(cpf)
else:
    print('Digite seu CPF corretamente e digite apenas números')
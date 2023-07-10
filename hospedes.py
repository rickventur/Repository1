quant = int(input('Quantas pessoas? '))
quartos = []

for i in range(quant):
    nome = str(input('Nome: '))
    cpf = str(input('CPF: '))
    hospedes = [nome, 'cpf: {}'.format(cpf)]
quartos.append(hospedes)
print(quartos.join())

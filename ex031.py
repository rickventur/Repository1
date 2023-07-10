distancia = int(input('Qual é a distância da sua viagem? '))
preco = distancia * 0.5

print('Você está pestes a começar um viagem de {}Km.'.format(distancia))
print('E o preço da sua passagem será de R${:.4}0'.format(preco))
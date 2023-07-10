import math

angulo = float(input('Digite o valor do angulo: '))
sin = math.sin(math.radians(angulo))
tang = math.tan(math.radians(angulo)) 
cos = math.cos(math.radians(angulo))

print('O seno, cosseno e tangente do ângulo {} são respectivamente: {:.2f}, {:.2f}, {:.2f}'.format(angulo, sin, tang, cos))
import random

print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

n = random.randint(1, 5)

resp = int(input('Em que numero eu pensei? '))
if resp == n:
    print('Você acertou, Parabéns!')
else:
    print('Você errou!')
        
f1 = 10000
f2 = 770
f3 = 2700

meta = 1000

if f1 >= meta and f1 < 2000:
    bonus = f1 * 10 / 100
    print('O funcionario 1 ganhou R${}0 de bônus!'.format(bonus))
elif f1 >= 2000:
    bonus = f1 * 15 / 100
    print('O funcionario 1 ganhou R${}0 de bônus!'.format(bonus))
else:
    print('O funcionario 1 ganhou 0 de bônus!')

if f2 >= meta and f2 < 2000:
    bonus = f2 * 10 / 100
    print('O funcionario 2 ganhou R${}0 de bônus!'.format(bonus))
elif f2 >= 2000:
    bonus = f2 * 15 / 100
    print('O funcionario 2 ganhou R${}0 de bônus!'.format(bonus))
else:
    print('O funcionario 2 ganhou 0 de bônus!')

if f3 >= meta and f3 < 2000:
    bonus = f3 * 10 / 100
    print('O funcionario 3 ganhou R${}0 de bônus!'.format(bonus))
elif f3 >= 2000:
    bonus = f3 * 15 / 100
    print('O funcionario 3 ganhou R${}0 de bônus!'.format(bonus))
else:
    print('O funcionario 3 ganhou 0 de bônus!')
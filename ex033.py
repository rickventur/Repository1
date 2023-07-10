a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('terceiro valor: '))

if a < b and a < c:
    print('{} é o menor valor'.format(a))
elif b < a and b < c:
    print('{} é o menor valor'.format(b))
else:
    print('{} é o menor valor'.format(c))

if a > b and a > c:
    print('{} é o maior valor'.format(a))
elif b > a and b > c:
    print('{} é o maior valor'.format(b))
else:
    print('{} é o maior valor'.format(c))



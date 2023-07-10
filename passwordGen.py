import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'

al = lower + upper + numbers
length = 16
password = ''.join(random.sample(al, length))
print(password)

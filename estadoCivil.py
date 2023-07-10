# Faça um programa que verifique o estado civil de uma pessoa. 
# Se a letra digitada é 'C' (Casado), 'S' (Solteiro), 'D' (Divorciado), 'V' (Viuvo), 'O' (Outro). 
# Conforme a letra escrita pelo usuario seu programa deve escrever o estado civil. 

print('C (Casado), S (Solteiro), D (Divorciado), V (Viuvo), O (Outro).')
estado_civil = str(input('Qual seu estado civil atual? '))

if estado_civil:
    if estado_civil == 'C':
        print('Você é Casado!')
    elif estado_civil == 'S':
        print('Você é Solteiro!')
    elif estado_civil == 'D':
        print('Você é Divorciado!')
    elif estado_civil == 'V':
        print('Você é Viuvo!')
    elif estado_civil == 'O':
        respf = str(input('Qual situação civil você se encontra? '))
        print('Você é {}'.format(respf))
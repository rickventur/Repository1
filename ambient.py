# Bibliotecas
import pyautogui
import time
import pandas as pd


pyautogui.PAUSE = 1
# Inicio da automação
pyautogui.press('win')
time.sleep(5)
pyautogui.write('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
pyautogui.press('enter')
# Navegador
time.sleep(5)
pyautogui.click(x=647, y=325)
pyautogui.write('caioaustim@gmail.com')
pyautogui.click(x=630, y=421)
pyautogui.write('c@34818263i0')
pyautogui.click(x=626, y=496)
# Google Drive
time.sleep(5)
pyautogui.click(x=870, y=308)
time.sleep(5)
pyautogui.click(x=909, y=619)
# Lendo a base de dados
tabela = pd.read_csv(r"C:\Users\Austin\Downloads\Compras.csv", sep=';')
print(tabela)

total_gasto = tabela['ValorFinal'].sum()
quantidade = tabela['Quantidade'].sum()
preco_medio = total_gasto / quantidade
print(total_gasto)
print(quantidade)
print(preco_medio)

import pyperclip

# Indo para o Gmail em nova guia no navegador
pyautogui.hotkey('ctrl','t')

time.sleep(5)
pyautogui.write('https://mail.google.com/mail/u/0/?hl=pt-BR#inbox?compose=newl')

time.sleep(5)
pyautogui.press('enter')

# Digitando E-mail
time.sleep(10)
pyautogui.click(x=78, y=150)
time.sleep(5)
pyautogui.write('katiabventura@gmail.com')

time.sleep(2)
pyautogui.press('tab')

# Assunto
time.sleep(2)
pyautogui.press('tab')

msg = 'Relatório da Empresa'
pyperclip.copy(msg)
pyautogui.hotkey('ctrl', 'v')

# Campo de texto
time.sleep(2)
pyautogui.click(x=756, y=362)

time.sleep(2)
pyautogui.click(x=793, y=402)
texto = ''' 
Prezados, 

Segue o relatório de compras

Total gasto: R$7.254.196,58
Quantidade de Produtos: 9.715
Preço Médio: R$746.70

Qualquer duvida e só falar.
Att., Rick do Python
'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')

# Finalizando Automação
time.sleep(2)
pyautogui.click(x=756, y=722)

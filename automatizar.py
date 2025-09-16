""" 
Entra no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
Faz o login 
Importa a base de dados
Cadastra os produtos
"""

import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5 # pause entre as execuções
tabela = pandas.read_csv("produtos.csv") # importa a tabela

# entra no chrome
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

time.sleep(1)

# entra no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") 
pyautogui.press("enter")

time.sleep(1)

# digita o email
pyautogui.press("tab")
pyautogui.write("oteteu@gmail.com") # escreve um email aleatório
pyautogui.press("tab")

# digita senha
pyautogui.write("1234567890") # senha aleatória 
pyautogui.press("enter")

# para cada item na tabela insere o nome de cada categoria do produto
for item in tabela.index: 
    codigo = str(tabela.loc[item, "codigo"])    
    marca = str(tabela.loc[item, "marca"])    
    tipo = str(tabela.loc[item, "tipo"])    
    categoria = str(tabela.loc[item, "categoria"])    
    preco_unitario = str(tabela.loc[item, "preco_unitario"])    
    custo = str(tabela.loc[item, "custo"])    
    obs = str(tabela.loc[item, "obs"])    
    
    pyautogui.scroll(100000) # sobe a página até o topo
    pyautogui.click(x=600, y=425) # clica na posição exata da primeira caixa de texto (para localizar a posição certa execute o código do arquivo 'auxiliar.py')
    
    pyautogui.write(codigo)
    pyautogui.press("tab")
    
    pyautogui.write(marca)
    pyautogui.press("tab")
    
    pyautogui.write(tipo)
    pyautogui.press("tab")
    
    pyautogui.write(categoria)
    pyautogui.press("tab")
    
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    
    pyautogui.write(custo)
    pyautogui.press("tab")
    
    if obs != "nan": # se o campo 'obs' voltar 'nan' (que é um campo vazio), não o preenche com 'nan'
        pyautogui.write(obs)
    pyautogui.press("enter")
    pyautogui.press("enter")
    
    time.sleep(1)
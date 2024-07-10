# Automatizando tarefa

''' 
    Cadastrar diversos produtos no sistema da empresa utilizando pyautogui
'''

# Importando o pyautogui e time
import pyautogui
import time

''' Alguns comandos do pyautogui '''
# pyautogui.write -> Escrever um texto
# pyautogui.press -> Aperta uma tecla
# pyautogui.click -> Clica em algum lugar da tela
# pyautogui.hotkey -> Combinação de teclas
# pyautogui.scroll -> Rola a tela para cima ou para baixo

# Define que depois de cada comando do pyautogui terá uma pausa de 0.3 segundos
pyautogui.PAUSE = 0.3

''' Passo 1 - Entrar no sistema da empresa '''

# Abrir o navegador (Chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Coloca o chrome em tela cheia
pyautogui.hotkey("win", "up")

# Entrar no sistema da empresa
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3) # Espera 3 segundos para continuar o código

''' Passo 2 - Fazer login '''

# Selecionar o campo de email 
pyautogui.click(x=498, y=381)

# Escreve o email do login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

# Passa para o próximo campo
pyautogui.press("tab")

# Escreve a senha
pyautogui.write("sua senha")

# Clica no botão de login
pyautogui.click(x=702, y=527)

# Espera 3 segundos
time.sleep(3)

''' Passo 3 - Importar a base de produtos para cadastrar '''

# Pandas trabalha com base de dados
import pandas as pd

# Lê a base de dados e armazena na variavel tabela
tabela = pd.read_csv("produtos.csv")

''' Passo 4 - Cadastra um produto '''

# Para cada linha da tabela irá repetir o seguinte bloco de comandos
for linha in tabela.index:
    # Clicar no campo de código
    pyautogui.click(x=617, y=257)       
    

    # Pega o valor do campo que a gente quer preencher da tabela e armazena em uma variável
    codigo = tabela.loc[linha, "codigo"]

    # Preenche o campo 
    pyautogui.write(str(codigo)) # str -> string

    # Passa para o próximo campo
    pyautogui.press("tab")

    ''' 
    Repetir o mesmo procceso nos outros campos 
    OBS: Em vez de criar uma variável ele já escreve direto dentro do pyautogui.write
    '''

    # MARCA
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    # TIPO
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    # CATEGORIA
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # PREÇO UNITÁRIO
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # CUSTO
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # OBSERVAÇÃO
    obs = tabela.loc[linha, "obs"]

    # Caso não tenha observação
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")

    # Cadastra produto
    pyautogui.press("enter")

    # Dá um scroll para cima para poder cadastrar o próximo produto
    pyautogui.scroll(5000) # px

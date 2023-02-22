import pyautogui
from time import sleep

# Primeiro vamos fazer o cadastro do Usuário
pyautogui.click(690,443, duration=1.5)
#=====================================#
pyautogui.click(700,389, duration=1.5)
pyautogui.write('Gildevan')
#=====================================#
pyautogui.click(728,414, duration=1.5)
pyautogui.write('123456')
#===FINALIZAR CADASTRO
pyautogui.click(664,442, duration=1.5)




# 1 - CLicar e digitar meu usuário
pyautogui.click(674,385,duration=1.5)
pyautogui.write('Gildevan')
# 2 - Clicar e digitar a senha
pyautogui.click(669,413,duration=1.5)
pyautogui.write('123456')
# 3 - Entrar no cadastro do Usuário
pyautogui.click(601,440,duration=1.5)

# Aqui ele vai pegar a lista cadastrada do Podutos
with open('programa_Otimizado/produtos.txt' , 'r') as file:
    for linha in file:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        #==========================
        pyautogui.click(392,373, duration=1.5)
        pyautogui.write(produto)

        pyautogui.click(401,400, duration=1.5)
        pyautogui.write(quantidade)

        pyautogui.click(387,425, duration=1.5)
        pyautogui.write(preco)

        pyautogui.click(319,582, duration=1.5)
        sleep(1)

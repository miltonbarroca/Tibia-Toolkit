import time
import pynput
import pyautogui
import os
import json
import random
import threading

# force use of ImageNotFoundException
pyautogui.useImageNotFoundException()

FOLDER_NAME = 'sqm_agua'
CONFIG_DEFAULT = 'default'
SQM_PEIXE = (88,92)

def create_folder():
    if not os.path.isdir(FOLDER_NAME):
        os.mkdir(FOLDER_NAME)

position = []
def getposition():
    global position
    x, y = pyautogui.position()
    posicao = {
        'x': x,
        'y': y
    }
    position.append(posicao)

def salvar_json(config):
    if os.path.isfile(f'{FOLDER_NAME}/{config}.json'):
        os.remove(f'{FOLDER_NAME}/{config}.json')
    with open(f'{FOLDER_NAME}/{config}.json','w') as file:
        file.write(json.dumps(position))

data = []
def ler_json(config):
    global data
    if os.path.isfile(f'{FOLDER_NAME}/{config}.json'):
        with open(f'{FOLDER_NAME}/{config}.json','r') as file:
                data = json.loads(file.read())
    else:
        print('Arquivo de configuracao nao encontrado !')

def girachar():
    pyautogui.keyDown('ctrl')  # hold down the ctrl key
    pyautogui.press('right')     # press the left arrow key
    time.sleep(0.3)
    pyautogui.press('down')     # press the left arrow key
    time.sleep(0.3)
    pyautogui.press('left')     # press the left arrow key
    time.sleep(0.3)
    pyautogui.press('up')     # press the left arrow key
    time.sleep(0.3)
    pyautogui.keyUp('ctrl')    # release the ctrl key

def fishing_rod(linha,coluna):
    sqm_centro = pyautogui.center()

contador = 0
def pescar():
    global contador
    while not event_th.is_set():
        random.shuffle(data)
        if event_th.is_set():
            return
        for item in data:
            if event_th.is_set():
                return
            coluna = item['x']
            linha = item['y']
            print('linha ', linha, ' Coluna ', coluna)
            for i in range(10):
                if event_th.is_set():
                    return
                print('usando vara de pesca...')
                #defina o hotkey F5 a fishing rod(vara)
                pyautogui.press('f5')
                time.sleep(0.5)
                print('movento mouse...')
                pyautogui.moveTo(coluna, linha)
                time.sleep(0.015)
                print('clicando mouse...')
                pyautogui.click(coluna, linha)
                time.sleep(0.5)
            #defina o espaco como tecla de troca o target(next target)
            pyautogui.press('space')
            time.sleep(0.5)
            contador = contador + 1
            if contador >= 15:
                if event_th.is_set():
                    return
                print('usando food...')
                #defina o hotkey F8 com food
                pyautogui.press('f8')
                time.sleep(0.5)
                print('usando exura ico...')
                #defina o hotkey F3 para o exura ico
                pyautogui.press('f3')
                time.sleep(0.5)
                #move o char para direita
                pyautogui.press('right')
                time.sleep(0.5)
                #move o char para esquerda
                pyautogui.press('left')
                time.sleep(0.5)
                #rotaciona o char
                girachar()
                contador = 0

running = False
def key_code(key):
    global running, config
    if key == pynput.keyboard.Key.esc:
        event_th.set()
        print('=============== Bot finalizado ====================')
        return False
    if hasattr(key, 'char') and key.char == 'g':
        if running == False:
            running = True
            create_folder()
            config = (input('Digite o nome da nova configuracao: '))
            print('Iniciando a gravacao de SQM !')
        else:
            running = False
            print('Salvando configuracao !')
            salvar_json(config)
            print('Parando a gravacao de SQM !')
    if hasattr(key, 'char') and key.char == 'p':
        print('Capturando posicao')
        getposition()
    if hasattr(key, 'char') and key.char == 'i':
        print('Lendo SQMs para pesca')
        ler_json(config)
        print('Iniciando pesca')
        th_pescar.start()

global event_th
event_th = threading.Event()
th_pescar = threading.Thread(target=pescar)

print('===================== Bot iniciado ==========================')
print('==    Digite a tecla [G] para iniciar a gravacao de SQM    ==')
print('==    Digite a tecla [P] para capturar a posicao do SQM    ==')
print('==    Digite a tecla [G] para finalizar a gravacao de SQM  ==')
print('==    Digite a tecla [i] para iniciar a pescaria           ==')
print('==    Digite a tecla [esc] para finalizar o bot            ==')
print('=============================================================')
global config
config = (input('Digite o nome da configuracao: '))
if config == "":
    print('Nenhuma configuracao digitada, default sera carregada!')
    config = CONFIG_DEFAULT
else:
    print(f'Carregando configuracao {config} digitada!')

with pynput.keyboard.Listener(on_press=key_code) as listener:
    listener.join()

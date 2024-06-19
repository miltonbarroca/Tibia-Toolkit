import random
import pyautogui as pg

PAUSA_VERIFICACAO = 0.5
ATK_SPELLS = ['9', '8', '9', '0']  # HOTKEYS das magias de ataque
EXETA = ['7']
UTITO = ['4']
ATK_COOLDOWNS = [random.uniform(2, 2.4) for _ in ATK_SPELLS]

SCRIPT_NAME = 'Exotic' #mude aqui quando for adicionar outra hunt pro bot

MINIMAP = (1753,26,108,112)

PIXEL_MANA = (996, 32)
COR_MANA = (44, 44, 44)

PIXEL_LIFE = (519, 34)
COR_LIFE = (39, 39, 39)

PIXEL_EXURA = (996, 32)
COR_EXURA = (44, 44, 44)

PIXEL_RING = (1768, 247)
COR_RING = (65, 68, 71)

PIXEL_COLAR = (1768, 181)
COR_COLAR = (70, 72, 75)

BATTLE_REGION = (1572, 24, 154, 51)
BATTLE_PLAYER = (0,25,171,51)

#0 - exori mas
#9 - exori
#8 - exori gran
#7 - exeta res
#6 - exori amp kor
#4 - utito tempo ou utamo

# def check():
#     while True:
#         box = pg.locateOnScreen('img/battle_player.png')
#         print(box)
#         pg.sleep(1)
# check()
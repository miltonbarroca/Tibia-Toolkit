import random
import pyautogui as pg

PAUSA_VERIFICACAO = 0.5
ATK_SPELLS = ['9', '8', '9', '0']  # HOTKEYS das magias de ataque
EXETA = ['7']
UTITO = ['4']
ATK_COOLDOWNS = [random.uniform(2, 2.4) for _ in ATK_SPELLS]

FOLDER_NAME = 'Feyrist_-1' #mude aqui quando for adicionar outra hunt pro bot

MINIMAP = (1753,26,108,112)

PIXEL_MANA = (979, 33)
COR_MANA = (34, 34, 35)

PIXEL_LIFE = (708, 32)
COR_LIFE = (41, 41, 41)

PIXEL_EXURA = (952, 34)
COR_EXURA = (36, 36, 36)

PIXEL_RING = (1768, 247)
COR_RING = (65, 68, 71)

PIXEL_COLAR = (1768, 181)
COR_COLAR = (70, 72, 75)

BATTLE_REGION = (1572, 24, 154, 51)

#0 - exori mas
#9 - exori
#8 - exori gran
#7 - exeta res
#6 - exori amp kor
#4 - utito tempo ou utamo

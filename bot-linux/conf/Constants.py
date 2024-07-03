import random
import pyautogui as pg

PAUSA_VERIFICACAO = 0.5
ATK_SPELLS = ['9', '8', '9', '0']  # HOTKEYS das magias de ataque
EXETA = ['7']
UTITO = ['4']
ATK_COOLDOWNS = [random.uniform(2, 2.4) for _ in ATK_SPELLS]

SCRIPT_NAME = 'centipe' #mude aqui quando for adicionar outra hunt pro bot
#SCRIPT_NAME = 'rotworm' #mude aqui quando for adicionar outra hunt pro bot
#SCRIPT_NAME = 'swamptroll' #mude aqui quando for adicionar outra hunt pro bot
#SCRIPT_NAME = 'orc' #mude aqui quando for adicionar outra hunt pro bot

MINIMAP = (1112, 70, 104, 111)

PIXEL_MANA = (1195, 33)
COR_MANA = (27, 27, 27)

PIXEL_LIFE = (609, 30)
COR_LIFE = (39, 39, 39)

PIXEL_EXURA = (952, 34)
COR_EXURA = (36, 36, 36)

PIXEL_RING = (1768, 247)
COR_RING = (65, 68, 71)

PIXEL_COLAR = (1768, 181)
COR_COLAR = (70, 72, 75)

BATTLE_REGION = (933, 71, 95, 40)
BATTLE_PLAYER = (0, 25, 171, 51)
RING_REGION = (1109, 271, 36, 37)

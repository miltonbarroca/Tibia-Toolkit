import random
import pyautogui as pg

Percentage = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]

LifeColorFull = [194, 74, 74]
LifeColor = [219, 79, 79]

ManaColorFull = [45, 45, 105]
ManaColor = [83, 80, 218]

BarSize = 92

PAUSA_VERIFICACAO = 0.5
ATK_SPELLS = ['9', '8', '9', '0']  # HOTKEYS das magias de ataque
EXETA = ['7']
UTITO = ['4']
ATK_COOLDOWNS = [random.uniform(2, 2.4) for _ in ATK_SPELLS]

SCRIPT_NAME = 'Exotic' #mude aqui quando for adicionar outra hunt pro bot

MINIMAP = (1753,26,108,112)

PIXEL_RING = (1768, 247)
COR_RING = (65, 68, 71)

PIXEL_COLAR = (1768, 181)
COR_COLAR = (70, 72, 75)

BATTLE_REGION = (1572, 24, 154, 51)
BATTLE_PLAYER = (0,25,171,51)

BARS_REGION = (1748,299,113,28)

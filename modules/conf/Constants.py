import random
import pyautogui as pg

PAUSA_VERIFICACAO = 0.5
ATK_SPELLS = ['9', '8', '9', '0']  # HOTKEYS das magias de ataque
EXETA = ['7']
UTITO = ['4']
ATK_COOLDOWNS = [random.uniform(2, 2.4) for _ in ATK_SPELLS]

FOLDER_NAME = 'Feyrist'

MINIMAP = (1753,26,108,112)

#0 - exori mas
#9 - exori
#8 - exori gran
#7 - exeta res
#6 - exori amp kor
#4 - utito tempo ou utamo
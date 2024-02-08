import random


PAUSA_VERIFICACAO = 0.5
ATK_SPELLS = ['0', '9', '8', '6']  # HOTKEYS das magias de ataque
EXETA = ['7']
UTITO = ['4']
ATK_COOLDOWNS = [random.uniform(2, 2.4) for _ in ATK_SPELLS]
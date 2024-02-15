
import threading
import keyboard
from modules.AutoCombo import auto_combo, pause, set_finalizar_programa

pause_programa = False
finalizar_programa = False

# Esperar pela tecla '=' antes de começar
print('Aguardando pela tecla "=" para iniciar...')
while True:
    if keyboard.is_pressed('='):
        break

# Iniciar threads após a tecla '=' ser pressionada
thread_combo_atk = threading.Thread(target=auto_combo)
thread_pause = threading.Thread(target=pause)

thread_combo_atk.start()
thread_pause.start()

# Aguardar até que o usuário pressione 'o' para finalizar o programa
while True:
    if keyboard.is_pressed('o'):
        set_finalizar_programa(True)
        break

# Aguardar até que as threads terminem
thread_combo_atk.join()
thread_pause.join()

print('Programa finalizado')

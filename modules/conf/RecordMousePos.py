from pynput import mouse, keyboard

# Lista para armazenar as coordenadas
coordenadas = []

# Contador para rastrear o número de coordenadas registradas
contador = 0

# Listener do mouse
mouse_listener = None

# Função para registrar a posição do mouse
def registrar_coordenadas(x, y):
    global coordenadas, contador
    if contador < 8:
        coordenadas.append((x, y))
        contador += 1
        print(f'Coordenada {contador}: {x}, {y}')
    if contador == 8:
        print("8 coordenadas registradas:")
        for i, coord in enumerate(coordenadas, start=1):
            print(f"Coordenada {i}: {coord}")
        encerrar_programa()

# Função para lidar com os eventos de teclado
def on_press(key):
    global mouse_listener
    try:
        if key == keyboard.Key.insert:
            if mouse_listener is None or not mouse_listener.running:
                mouse_listener = mouse.Listener(on_click=on_click)
                mouse_listener.start()
        elif key == keyboard.Key.esc:
            encerrar_programa()
    except AttributeError:
        pass

# Função para lidar com os cliques do mouse
def on_click(x, y, button, pressed):
    if pressed:
        registrar_coordenadas(x, y)

# Função para encerrar o programa
def encerrar_programa():
    global mouse_listener, keyboard_listener
    if mouse_listener is not None:
        mouse_listener.stop()
    keyboard_listener.stop()
    print("Programa encerrado.")

# Iniciando o ouvinte do teclado
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()
keyboard_listener.join()

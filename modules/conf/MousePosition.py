from pynput import keyboard, mouse
from PIL import ImageGrab

def on_press(key):
    try:
        if key == keyboard.Key.insert:
            mouse_controller = mouse.Controller()
            x, y = mouse_controller.position
            img = ImageGrab.grab()
            rgb = img.getpixel((x, y))
            print(f"Coordenadas do mouse: ({x}, {y}), RGB: {rgb}")
        elif key == keyboard.Key.esc:
            print("Encerrando programa...")
            return False
    except Exception as e:
        print(f"Erro: {e}")

def main():
    print("Pressione Insert para obter as coordenadas e a cor RGB do mouse...")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
